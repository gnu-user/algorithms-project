#!/usr/bin/env python
#
# The following is a proof-of-concept project that implements various algorithms
# for determining if a point is inside a polygon. Primarily we are focused only
# on convex polygons as they apply to our convex hull solution.
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
# 
from termcolor import colored
from numpy import dot, arccos, sqrt
from numpy.random import *
from matplotlib.pyplot import *
import matplotlib.lines
from time import sleep

# A function which handles the first edge case for the pnpoly algorithm. If
# a vector lies on the vertical or horizontal edge between two vertices of the
# hull then it is cnosidered as being a point within the null
# TODO, this only applies for vectors of 2 dimensional space
# TODO, I hate how this is implemented....there is a much cleaner solution
# @return true if the point lies on the horizontal or vertical edge between the
# the two vertices
def vert_horz_edge(vertices, point):
    x_lower = 0
    x_upper = 0
    y_lower = 0
    y_upper = 0
    on_edge = False
    
    # If edge between the vertices forms a horizontal or vertical edge
    if (((vertices[0].x == vertices[1].x) or (vertices[0].y == vertices[1].y))):
        # Set the x and y edge lower and upper boundaries
        if (vertices[0].x > vertices[1].x):
            x_upper = vertices[0].x
            x_lower = vertices[1].x
        else:
            x_upper = vertices[1].x
            x_lower = vertices[0].x
        if (vertices[0].y > vertices[1].y):
            y_upper = vertices[0].y
            y_lower = vertices[1].y
        else:
            y_upper = vertices[1].y
            y_lower = vertices[0].y
        
        # If the point lies on the horizonal or vertical line, check if it lies
        # on the edge between the two vertices
        if (point.x == vertices[0].x):
            if (point.y >= y_lower and point.y <= y_upper):
                on_edge = True
        # If the point lies on the horizontal line
        elif (point.y == vertices[0].y):
            if (point.x >= x_lower and point.x <= x_upper):
                on_edge = True
    
    return on_edge


# The following is an implementation called PNPOLY the following is a link
# to the source, it is a clever solution which handles boundary edges and
# other corner cases
# 
# SEE: http://www.ecse.rpi.edu/Homepages/wrf/Research/Short_Notes/pnpoly.html
#
# pnpoly -- determine if a point is within a convex polygon
#
# @param veritices An array consisting of tuples of x,y for vertices of the polygon
# @param point The point to check if it's in the polygon, the  x,y tuple
#
# @return True if the point is inside the polygon, false otherwise
#
# TODO this fails for some points due to the limits of finite arithmetics, add
# support for an EPSILON threshold so that points such as sqrt(2)/2 would be
# within the unit circle
def pnpoly(vertices, point):
    i = 0
    j = len(vertices) - 1
    inside_poly = False
    
    while(i < len(vertices)):
        # Handle the edge case where the vector lies on a horizontal or vertical
        # edge between two vertices
        if (vert_horz_edge([vertices[j], vertices[i]], point)):
            # point lies on edge, which is within polygon
            return True
        # If the vector does not lie on a horizontal or vertical edge then verify
        # that the point is b/w the current and previous vertex y axis
        elif (((vertices[i].y > point.y) != (vertices[j].y > point.y))
            # If the point's x value is less than the delta of current and prev.
            # vertex x value mult. by the rate of change of the y values add
            # the current vertex's x value
            # I don't fully understand how this works.. I need to write it out
            and (point.x < (vertices[j].x - vertices[i].x) * 
                (point.y - vertices[i].y) / (vertices[j].y - vertices[i].y) 
                + vertices[i].x)):
                    # Inverse the result each time
                    inside_poly = not inside_poly
        j = i
        i += 1
        
    return inside_poly
   
# Calculates the angle between 2 vectors in radians
def angle_calc(p1,p2,origin):
    a = Vector(p1.x-origin.x, p1.y-origin.y)
    b = Vector(p2.x-origin.x, p2.y-origin.y)
    return arccos((dot([a.x,a.y], [b.x,b.y]))/(a.mag*b.mag))

# Returns the index of the first point of the pair vectors within
# the hull that result in the maximum interior angle

#TODO check if the angle between 2 points results in 0
#therefore the point to be added is on the line, take the one further
#away and remove the other
#TODO point at origin, does not work since magnitude is 0
def max_interior_angle(hull, point):
    i = 0
    j = len(hull) - 1
    max_angle = 0
    angle = 0
    index = -1    #if returns -1 this is invalid!!!!
    while(i < len(hull)):
       angle = angle_calc(hull[j],hull[i], point)
       print("point j {}, point i {}, angle {}".format([hull[j].x, hull[j].y], [hull[i].x, hull[i].y], angle))
       if (max_angle < angle):
           max_angle = angle
           index = i
       j = i
       i += 1
    return index

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mag = np.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return "(x=%f, y=%f, mag=%f)" % (self.x, self.y, self.mag)
    
def init_vectors(points):
    vectors = []
    for point in points:
        vectors.append(Vector(point[0], point[1]))
    return vectors

def quicksort (list):
    """
    Quicksort using list comprehensions
    >>> qsort1<<docstring test numeric input>>
    <<docstring test numeric output>>
    >>> qsort1<<docstring test string input>>
    <<docstring test string output>>
    """
    if list == []: 
        return []
    else:
        pivot = list[0]
        lesser = quicksort([x for x in list[1:] if x.mag < pivot.mag])
        greater = quicksort([x for x in list[1:] if x.mag >= pivot.mag])
        return greater + [pivot] + lesser

###############################################################################
#The following notes no longer apply, they are important however to help with #
#defining why we are using the current approach.                              #
###############################################################################
#Need to take the interior angle of the points the new points connects to
#The check is if the interior angle is <180 given the addition of the new point
#   IF the angle is < 180 the point is kept
#   IF the angle is > 180 the point is discarded (therefore the new point is 
#       connected to the point following the given point).
#       This point is then checked for it's angle to determine if it is also valid, and so on (until condition 1 is met)
#   IF the angle is = 180 then the point is on the same line 
#       Need to determine how to cover this case
#       Most likely the point is discarded (since it is on the same line as the other point)
#Since Dot Product will only return an angle < 180, since it calculates the lowest angle between the vectors
#Cross product needs to be used to determine whether the orthogonal vector is pointing into or out of the page
#   IF the orthogonal vector is pointing outside the page
#       left, down or up
#   IF the orthogonal vector is pointing into the page
#       right down or up

#This is broken at the moment because the angle calculator will alway return angles less than 180 because it is the dot product therefore it is finding the smaller angle.
#def pos_check(vectors, index):
#    if (float)(angle_calc(vectors[index], vectors[(index+2)%len(vectors)], vectors[(index+1)%len(vectors)])) > pi:
#        vectors.remove((index+1)%len(vectors))
#        pos_check(vectors, index)

#def neg_check(vectors, index):
#    if (float)(angle_calc(vectors[index], vectors[(index-2)%len(vectors)], vectors[(index-1)%len(vectors)])) > pi:
#        vectors.remove((index-1)%len(vectors))
#        neg_check(vectors, index)


#Through use of pnpoly check if given the remove of the point (at index + 1)
#next to the point at the given index the point will be within the polygon
def pos_check(vectors, index):
    point = vectors[(index+1)%len(vectors)]
    del(vectors[(index+1)%len(vectors)])
    print (point.x, point.y)
    if pnpoly(vectors, point):
        if index > ((index+1)%len(vectors)):
            index = index-1
        print ("pos", vectors[index].x, vectors[index].y, index)
        pos_check(vectors, index)
    else:
        vectors.insert((index+1)%len(vectors), point)

#Through use of pnpoly check if given the remove of the point (at index - 1)
#next to the point at the given index the point will be within the polygon
def neg_check(vectors, index):
    point = vectors[(index-1)%len(vectors)]
    del(vectors[(index-1)%len(vectors)])
    print (point.x, point.y)
    if pnpoly(vectors, point):
        if index > ((index-1)%len(vectors)):
            index = index-1
        print ("neg", vectors[index].x, vectors[index].y, index)
        neg_check(vectors, index)
    else:
        vectors.insert((index-1)%len(vectors), point)

def convex_check(vectors, index):
    pos_check(vectors,index)
    neg_check(vectors,index)


def add_vertex(hull, point):
    if not pnpoly(hull, point):
        index = max_interior_angle(hull, point)
        hull.insert(index, point)
        for vertex in hull:
            print(vertex)
        convex_check(hull, index)



# Initialize the plot axis and title
axis([0, 100, 0, 100])
title('Convex Hull')

# Test case, test points on the line, etc..
#points = [(1, 1), (1, 3), (2,4), (3, 3), (3,1)]

# Test case, random points entered by a simulated user
#points = [(1, 1), (1, 3), (2,4), (3, 3), (3,1), (3,6)]
#shuffle(points)

#triangle test case
#points = [(2, 10), (2, -4), (-2, -3)]

# Generate a set of random points to test
#x_points = randint(8, size=10)
#y_points = randint(8, size=10)
#y_points = rand(2, 10)

# Get user input
user_points = ginput(n=0,timeout=0, show_clicks=True)

#for i in range(len(x_points)):
#    x_points[i] += 1
#    y_points[i] += 1

#points = list(zip(x_points, y_points))
# Perform a map to convert all vertices to floating points and user input to float
# this is the only way to guarantee floating point precision for all operations
for point in user_points:
    map(float, point)
    print(point)

vectors = init_vectors(user_points)

# Step 1, sort the vectors by magnitude
vectors = quicksort(vectors)

# Remove duplicate points, we only want distinct points
vectors_del = []
for i in range(len(vectors)-1):
    if (vectors[i].x, vectors[i].y) == (vectors[i+1].x, vectors[i+1].y):
        print('Duplicate points: ', vectors[i], vectors[i+1])
        vectors_del.append(i+1)

j = 0
for i in vectors_del:
    del vectors[i - j]
    j += 1

#print(angle_calc(Vector(0,0),Vector(3,4), Vector(3,2)))
#index = max_interior_angle(vectors, Vector(3, -1))

#index = max_interior_angle(vectors, Vector(0, 0))

#print(vectors[index].x, vectors[index].y)
#if (index + 1 >= len(vectors)):
#    index = -1
#print(vectors[index+1].x, vectors[index+1].y)

#add_vertex(vectors, Vector(3,6))



# Plot all of the vectors
plot(
    [vector.x for vector in vectors],
    [vector.y for vector in vectors], 
    'ro'
)

# Step 2, create the base hull, which is the greatest magnitude
# the least magnitude, and 2nd greatest magnitude
hull = [vectors.pop(0), vectors.pop(-1), vectors.pop(0)]

print("BASE HULL")
for vertex in hull:
    print(vertex)

# Now, for each point in the plot add it to convex hull if it satisfies the
# axioms for a vertex of the hull
print("\n")
for vector in vectors:
    add_vertex(hull, vector)


# Add the first vector in the hull to the end of the hull to simplify plotting
hull.append(hull[0])

# Plot the hull
for i in range(len(hull)):
    print(hull[i].x, hull[i].y, hull[i].mag )
    plot(
        [vertex.x for vertex in hull[:i+1]],
        [vertex.y for vertex in hull[:i+1]],
        color='b', linewidth=1.5, antialiased=True
    )
    draw()
#    sleep(1.0)
#del hull[-1]

show()


# Get a user to enter a point
#while True:
#    raw_point = input("Enter a point's x and y coordinates: ")
#    usr_point = tuple(map(float,raw_point.split(',')))
#
#    if (pnpoly(points, usr_point) == True):
#        print(colored("The point is within the polygon", 'green'))
#    else:
#        print(colored("The point is NOT within the polygon",'red'))