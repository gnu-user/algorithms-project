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

def cross(o, a, b):
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

def convex_hull(vectors):

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


axis([0, 10, 0, 10])
title('Convex Hull')
grid(True)

# Get user input
user_points = ginput(n=0,timeout=0, show_clicks=True)

for point in user_points:
    map(float, point)
    print(point)

#points = sorted(set(points))
points = sorted(set(user_points))
vectors = init_vectors(points)

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

# Plot all of the vectors
plot(
    [vector.x for vector in vectors],
    [vector.y for vector in vectors], 
    'ro'
)

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
    #print(hull[i].x, hull[i].y)
    plot(
        [vertex.x for vertex in hull[:i+1]],
        [vertex.y for vertex in hull[:i+1]],
        linewidth=1.5, antialiased=True
    )
    draw()
#        sleep(0.5)
#    del hull[-1]

show()


