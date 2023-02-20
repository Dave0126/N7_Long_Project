import math
import socket
import json

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

class Area:
    def __init__(self, area_shape = "Polygon", coordinates = []):
        self.area_shape = area_shape
        self.coordinates = coordinates
        self.restricted = False
        self.n_vertices = 0

    def change_restriction(self):
        self.restricted = not(self.restricted)

    def set_data_from_file(self, file, index) :
        f = open(file)
        shapes = json.load(f)

        self.coordinates = shapes["features"][index]["geometry"]["coordinates"][0]
        self.area_shape = shapes["features"][index]["geometry"]["type"]
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
            side = Line(Point(self.coordinates[i]), Point(self.coordinates[(i + 1) % self.n_vertices]))
            if (side.isIntersect(exline)):
    
                # If side is intersects exline
                if (direction(side.p1, p, side.p2) == 0):
                    return side.onLine(p)
                count += 1
            i = (i + 1) % self.n_vertices
    
        # When count is odd
        return not((count % 2) == 0)
        
    def __str__(self):
        return f"Area of shape {self.area_shape}, restricted : {self.restricted}"
    