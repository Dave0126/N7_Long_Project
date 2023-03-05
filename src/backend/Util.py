import json
import math
import os.path

import geojson as geojson
from PIL import Image

import shapely.geometry
from shapely import affinity, LineString, Point
from shapely.geometry import shape
import numpy as np
import heapq
import math
import os

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def loadGeoJsonFile(obstacles, fileName):
    with open(fileName) as f:
        data = json.load(f)

    # Parse to shapely.Polygon
    for feature in data["features"]:
        geom = shape(feature["geometry"])
        if geom.type == "Polygon":
            obstacles.append(geom)
        elif geom.type == "MultiPolygon":
            for sub_geom in geom:
                obstacles.append(sub_geom)


def jsonToGrid(map, resolution, startPoint, endPoint, obstacles):
    bounds = map.bounds
    print(bounds)
    rows = int(np.ceil((bounds[3] - bounds[1]) / resolution))
    cols = int(np.ceil((bounds[2] - bounds[0]) / resolution))
    # 初始化网格 Initialize the grid
    grid = np.zeros((rows, cols))
    print(str(rows) + "\t" + str(cols))
    # 计算网格索引 Calculating the grid index
    for i in range(rows):
        for j in range(cols):
            x = bounds[0] + j * resolution
            y = bounds[1] + i * resolution
            point = shapely.geometry.Point(x, y)
            if (startPoint.almost_equals(point, decimal=3)):
                grid[rows - i - 1, j] = -1
                start = (rows - i - 1, j)
            if (endPoint.almost_equals(point, decimal=3)):
                grid[rows - i - 1, j] = -2
                end = (rows - i - 1, j)
            for polygon in obstacles:
                if polygon.contains(point):
                    grid[rows - i - 1, j] = 1
                    break
    print(grid)
    return grid, start, end


def heuristic(a, b):
    """
    计算从点a到点b的启发式距离
    Calculate the heuristic distance from point a to point b
    """
    if a is None or b is None:
        raise ValueError("无法使用 None 值计算启发式 Heuristic cannot be calculated using None values")
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def astar(array, start, goal):
    """
    使用A*算法搜索从起点到终点的最短路径
    Search for the shortest path from the start to the end using the A* algorithm
    """
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))

    while oheap:

        current = heapq.heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data[::-1]

        close_set.add(current)

        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j

            tentative_g_score = gscore[current] + heuristic(current, neighbor)

            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    continue
            else:
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))

    return None


def saveAsGridImage(gridMap, path):
    # 创建一个新的图像，将所有像素设置为黑色 Create a new image with all pixels set to black
    img = Image.new('RGB', (gridMap.shape[1], gridMap.shape[0]), (255, 255, 255))
    # 将网格数据复制到像素值中 Copy grid data to pixel values
    for i in range(gridMap.shape[0]):
        for j in range(gridMap.shape[1]):
            if gridMap[i, j] == 1:
                # 如果网格中的值为 1，则将像素设置为白色 If the value in the grid is 1, then set the pixel to white
                img.putpixel((j, i), (0, 0, 0))
            if gridMap[i, j] == -1:
                # 如果网格中的值为 -1，则将像素设置为红色（起点） If the value in the grid is -1, set the pixel to red (starting point)
                img.putpixel((j, i), (255, 0, 0))
            if gridMap[i, j] == -2:
                # 如果网格中的值为 -1，则将像素设置为绿色（起点）If the value in the grid is -1, set the pixel to green (starting point)
                img.putpixel((j, i), (0, 255, 0))
    for p in path:
        img.putpixel((p[1], p[0]), (0, 0, 255))
    # 保存图像 Save image
    img.save(ROOT_PATH + "/demos/grid.png")

def findNonCollinearPoints(coords):
    non_collinear_points = [coords[0]]
    for i in range(1, len(coords)-1):
        x1, y1 = coords[i-1]
        x2, y2 = coords[i]
        x3, y3 = coords[i+1]

        # 计算向量 Calculating vectors
        vec1 = (x1 - x2, y1 - y2)
        vec2 = (x3 - x2, y3 - y2)

        # 计算向量夹角的cos值 Calculate the cosine of the vector angle
        cos_theta = (vec1[0]*vec2[0] + vec1[1]*vec2[1]) / (math.sqrt(vec1[0]**2 + vec1[1]**2) * math.sqrt(vec2[0]**2 + vec2[1]**2))

        # 角度小于等于直线的两条边平行的情况，角度为180度
        # Angle less than or equal to the case where two sides of a line are parallel, angle 180 degrees
        if abs(cos_theta) < 1:
            angle = math.acos(cos_theta) * 180 / math.pi
            if abs(angle - 180) > 1e-6:
                non_collinear_points.append(coords[i])
    non_collinear_points.append(coords[-1])

    return non_collinear_points


def gridToJsonAndSaveAsFile(point_list, non_collinear_points, saveJsonFileNAme, map, resolution, endPoint):
    rows = int(np.ceil((map.bounds[3] - map.bounds[1]) / resolution))
    cols = int(np.ceil((map.bounds[2] - map.bounds[0]) / resolution))
    for node in non_collinear_points:
        x = map.bounds[0] + node[1] * resolution
        y = map.bounds[1] + (rows - node[0] - 0.5) * resolution
        point = shapely.geometry.Point(x, y)
        point_list.append(point)
    point_list.append(endPoint)

    line = LineString([point.coords[0] for point in point_list])

    # 将LineString对象转换为GeoJSON格式 Converting LineString objects to GeoJSON format
    feature = geojson.Feature(geometry=line, properties={})
    feature_collection = {
        "type": "FeatureCollection",
        "features": [feature]
    }

    geojson_object = geojson.dumps(feature_collection, indent=4)
    with open(saveJsonFileNAme, 'w') as f:
        f.write(geojson_object)


def createPath(startPoint  = shapely.geometry.Point(1.425299, 43.596458) , endPoint  = shapely.geometry.Point(1.453875, 43.608208)):
    obstacles = []
    loadGeoJsonFile(obstacles, ROOT_PATH + '/data/tests/backend/map.json')

    # 网格分辨率 Grid resolution : 1/10000 * 111km
    resolution = 1 / 10000
    map = shapely.geometry.MultiPolygon(obstacles)
    map = map.union(startPoint)
    map = map.union(endPoint)
    gridMap, start, goal = jsonToGrid(map, resolution, startPoint, endPoint, obstacles)

    # Run a_star
    path = astar(np.array(gridMap), start, goal)
    print(path)

    # Sets of coordinates that are not co-linear
    nonCollinearPoints = findNonCollinearPoints(path)
    print(nonCollinearPoints)

    GeoJsonPointList = [startPoint]
    gridToJsonAndSaveAsFile(GeoJsonPointList, nonCollinearPoints, ROOT_PATH+'/data/temp/customLines/FP_00000002_202302281115.json', map, resolution, endPoint)

    saveAsGridImage(gridMap, path)