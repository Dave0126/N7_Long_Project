import math
import socket
import json
from src.backend.classes.Area import Area

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def direction(a, b, c):
    val = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y)

    if (val == 0):

        # Colinear
        return 0

    elif (val < 0):

        # Anti-clockwise direction
        return 2

    # Clockwise direction
    return 1

def read_json(file):
    f = open(file)
    return json.load(f)["features"]

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def onLine(self, p):
        # Check whether p is on the line or not
        if (p.x <= max(self.p1.x, self.p2.x)
            and p.x <= min(self.p1.x, self.p2.x)
            and (p.y <= max(self.p1.y, self.p2.y)
                and p.y <= min(self.p1.y, self.p2.y))):
            return True
    
        return False

    def isIntersect(self, other_line):
        # Four direction for two lines and points of other line
        dir1 = direction(self.p1, self.p2, other_line.p1)
        dir2 = direction(self.p1, self.p2, other_line.p2)
        dir3 = direction(other_line.p1, other_line.p2, self.p1)
        dir4 = direction(other_line.p1, other_line.p2, self.p2)
    
        # When intersecting
        if (dir1 != dir2 and dir3 != dir4):
            return True
    
        # When p2 of line2 are on the line1
        if (dir1 == 0 and self.onLine(other_line.p1)):
            return True
    
        # When p1 of line2 are on the line1
        if (dir2 == 0 and self.onLine(other_line.p2)):
            return True
    
        # When p2 of line1 are on the line2
        if (dir3 == 0 and other_line.onLine(self.p1)):
            return True
    
        # When p1 of line1 are on the line2
        if (dir4 == 0 and other_line.onLine(self.p2)):
            return True
    
        return False

def extract_zones(zones_list, json_text):
    shapes = json.load(json_text)["features"]
    for i in range(len(shapes)) :
        current = Zone(i, shapes[i]["geometry"]["type"], shapes[i]["geometry"]["coordinates"][0])
        zones_list.append(current)
    return zones_list

def extract_zones_from_file(zones_list, json_file):
    f = open(json_file)
    shapes = json.load(f)["features"]
    for i in range(len(shapes)) :
        current = Zone(i, shapes[i]["geometry"]["type"], shapes[i]["geometry"]["coordinates"][0])
        zones_list.append(current)
    return zones_list

def distance(x1, y1, x2, y2):
    dist = math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
    return dist

def min_dist_ext(p, zone_coords):
    zone = Zone("param_zone", coordinates=zone_coords)
    if not(zone.checkInside(Point(p[0], p[1]))):
        return
    min_dist = math.inf
    best_point = None
    for i in range(len(zone_coords)):
        for j in range(1, len(zone_coords) + 1):
            p1 = zone_coords[i]
            p2 = zone_coords[j]
            p21Dir = [p2[0] - p1[0], p2[1] - p1[1]]
            perpDir = [-p21Dir[1], p21Dir[0]]
            p31Dir = [p[0] - p1[0], p[1] - p1[1]]
            s = (perpDir[1] * p31Dir[0] - perpDir[0] * p31Dir[1]) / (p21Dir[0] * perpDir[1] - p21Dir[1] * perpDir[0])
            Intersect = [p1[0] + s* p21Dir[0], p1[1] + s* p21Dir[1]]
            dist = distance(p[0], p[1], Intersect[0], Intersect[1])
            if (dist < min_dist):
                min_dist = dist
                best_point = Intersect
    return Intersect

class Zone:
    def __init__(self, zoneLabel, zone_shape = "Polygon", coordinates = [], description = "", area_type = Area()):
        self.label = zoneLabel
        self.zone_shape = zone_shape
        self.coordinates = coordinates
        self.restricted = False
        self.n_vertices = len(self.coordinates)
        self.area_type = area_type
        self.description = description

    def change_restriction(self):
        self.restricted = not(self.restricted)

    def change_area_type(self, new_area_type):
        self.area_type = new_area_type

    def change_zone_description(self, new_desc):
        self.description = new_desc

    def set_data_from_file(self, file, index) :
        f = open(file)
        shapes = json.load(f)["features"]

        self.coordinates = shapes[index]["geometry"]["coordinates"][0]
        self.area_shape = shapes[index]["geometry"]["type"]
        self.n_vertices = len(self.coordinates)

    def checkInside(self, p):
    
        # When polygon has less than 3 edge, it is not polygon
        if (self.n_vertices < 3):
            return False
    
        # Create a point at infinity, y is same as point p
        exline = Line(p, Point(9999, p.y) )
        count = 0
        i = 1
        first_loop = True
        while(i != 0):
            if first_loop :
                i  = 0
                first_loop = False
                
            # Forming a line from two consecutive points of
            # poly
            side = Line(Point(self.coordinates[i][0], self.coordinates[i][1]), Point(self.coordinates[(i + 1) % self.n_vertices][0], self.coordinates[(i + 1) % self.n_vertices][1] ))
            if (side.isIntersect(exline)):
    
                # If side is intersects exline
                if (direction(side.p1, p, side.p2) == 0):
                    return side.onLine(p)
                count += 1
            i = (i + 1) % self.n_vertices
    
        # When count is odd
        return not((count % 2) == 0)
        
    def __str__(self):
        return f"Zone of shape {self.area_shape}, restricted : {self.restricted}"
    