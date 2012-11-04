#!/usr/bin/env python
#
# The following is a proof-of-concept project that implements various algorithms
# for determining if a point is inside a polygon. Primarily we are focused only
# on convex polygons as they apply to our convexhull solution.
#
# See the following topics for more information:
# 
# http://en.wikipedia.org/wiki/Convex_hull
# http://en.wikipedia.org/wiki/Carath%C3%A9odory%27s_theorem_(convex_hull)
# http://en.wikipedia.org/wiki/Convex_polygon
# 
# http://en.wikipedia.org/wiki/Point_in_polygon
# http://en.wikipedia.org/wiki/Winding_number
# http://en.wikipedia.org/wiki/Jordan_curve_theorem
#
# http://en.wikipedia.org/wiki/Polygon_triangulation
# http://www.codeforge.com/article/76159
from math import sqrt

# The following is an implementation called PNPOLY the following is a link
# to the source, it is a clever solution which handles boundary edges and
# other corner cases
# 
# SEE: http://www.ecse.rpi.edu/Homepages/wrf/Research/Short_Notes/pnpoly.html
#
# pnpoly -- determine if a point is within a convex polygon
# @param veritices An array consisting of tuples of x,y for vertices of the polygon
# @param point The point to check if it's in the polygon, the  x,y tuple
def pnpoly(vertices, point):
    i = 0
    j = len(vertices) - 1
    within_line = False
    
    while(i < len(vertices)):
        # First verify that the point is b/w the current and previous vertex y axis
        if (((vertices[i][1] > point[1]) != (vertices[j][1] > point[1]))
            # If the point's x value is less than the delta of current and prev.
            # vertex x value mult. by the rate of change of the y values add
            # the current vertex's x value
            # I don't fully understand how this works.. I need to write it out
            and (point[0] < (vertices[j][0] - vertices[i][0]) * 
                (point[1] - vertices[i][1]) / (vertices[j][1] - vertices[i][1]) 
                + vertices[i][0])):
                within_line = not within_line
        j = i
        i += 1
    return within_line


vertices = [(1,3), (3,2), (4,2), (-2,4), (-5,3), (2,-4), (3,-6), (-5,-9), (-4,-5)]
#vertices = [(1, 1), (13, 13), (25, 1)]

# Perform a map to convert all vertices to floating points and user input to float
# this is the only way to guarantee floating point precision for all operations
for vertex in vertices:
    map(float, vertex)

# Get a user to enter a point
raw_point = input("Enter a point's x and y coordinates: ")
point = tuple(map(float,raw_point.split(',')))

if (pnpoly(vertices, point) == True):
    print("The point is within the polygon")
else:
    print("The point is not within the polygon")
