from termcolor import colored
from numpy import dot, arccos, sqrt
from numpy.random import *
from matplotlib.pyplot import *
import matplotlib.lines
from time import sleep

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(x=%f, y=%f)" % (self.x, self.y)

def init_vectors(points):
    vectors = []
    for point in points:
        vectors.append(Vector(point[0], point[1]))
    return vectors

#Need to adjust the so it will sort by x and then sort by y
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
        lesser = quicksort([x for x in list[1:] if x.x < pivot.x])
        greater = quicksort([x for x in list[1:] if x.x >= pivot.x])
        return greater + [pivot] + lesser

def cross(o, a, b):
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

def convex_hull(vectors):
    #vector = quicksort(vector)

    #vectors = 
    if len(vectors) <= 1:
        return vectors

    #Build lower hull
    lower = []
    for p in vectors:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    #Build higher hull
    upper = []
    for p in reversed(vectors):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


axis([0, 100, 0, 100])
title('Convex Hull')
grid(True)

# Test case, test points on the line, etc..
#points = [(1, 1), (1, 3), (2,4), (3, 3), (3,1)]

# Test case, random points entered by a simulated user
#points = [(1, 1), (1, 3), (2,4), (3, 3), (3,1), (3,6)]
#shuffle(points)

#triangle test case
#points = [(2, 10), (2, -4), (-2, -3)]

# Generate a set of random points to test
x_points = randint(95, size=100)
y_points = randint(95, size=100)

# Get user input
#user_points = ginput(n=0,timeout=0, show_clicks=True)

# Do this show that is shows the hull being drawn
user_points = ginput(n=0,timeout=0, show_clicks=False)

# Adjust the point bounds so that they are in the range [1..9]
for i in range(len(x_points)):
    x_points[i] += 1
    y_points[i] += 1

points = list(zip(x_points, y_points))

# Perform a map to convert all vertices to floating points and user input to float
# this is the only way to guarantee floating point precision for all operations
for point in points:
    map(float, point)
    print(point)

points = sorted(set(points))
vectors = init_vectors(points)

# Step 1, sort the vectors by magnitude
#vectors = quicksort(vectors)

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
#hull = [vectors.pop(0), vectors.pop(-1), vectors.pop(0)]

#print("BASE HULL:")
#for vertex in hull:
#    print(vertex)

# Now, for each point in the plot add it to convex hull if it satisfies the
# axioms for a vertex of the hull
print("\n")
#for vector in vectors:
#    add_vertex(hull, vector)
hull = convex_hull(vectors)


    # Add the first vector in the hull to the end of the hull to simplify plotting
hull.append(hull[0])
    # Plot the hull


print("FINAL POINTS IN CONVEX HULL:")
for vertex in hull:
    print(vertex)

for i in range(len(hull)):
    print(hull[i].x, hull[i].y)
    plot(
        [vertex.x for vertex in hull[:i+1]],
        [vertex.y for vertex in hull[:i+1]],
        linewidth=1.5, antialiased=True
    )
    draw()
#        sleep(0.5)
#    del hull[-1]

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

