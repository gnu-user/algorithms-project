#!/usr/bin/env python
#
# A simple test of different pyplotting functions, the
# goal is to have a simple solution that can take in user
# input and output a plot of the points connected
import numpy as np
from matplotlib.pyplot import *
#from matplotlib.pyplot import plot, ginput, scatter, show, axis, hold
import matplotlib.lines

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mag = np.sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        return "(x=%f, y=%f, mag=%f)" % (self.x, self.y, self.mag)

# Initialize the plot axis and title
axis([0, 100, 0, 100])
title('Convex Hull')

# Get user input
user_points = ginput(n=0,timeout=0, show_clicks=True)

# Support for lambda tuple arguments removed in python 3 because guido is a fucking idiot
# points = map(lambda (x, y): Point(x, y), user_points)

# Convert input as a list of points
points = []
for point in user_points:
    points.append(Point(point[0],point[1]))

# Add the first point to the end of the list
points.append(points[0])


print(points)

# Plot the users input
plot(
    [point.x for point in points],
    [point.y for point in points]
)

show()