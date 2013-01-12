#!/usr/bin/env python

##############################################################################
# 
#  ENGR 3770U -- Design and Analysis of Algorithms -- Final Project
#
#  Copyright (C) 2012, Jonathan Gillett, Joseph Heron
#  All rights reserved.
#
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

#
# A simple test of different pyplotting functions, the
# goal is to have a simple solution that can take in user
# input and output a plot of the points connected
import numpy as np
from matplotlib.pyplot import *
#from matplotlib.pyplot import plot, ginput, scatter, show, axis, hold
import matplotlib.lines
from time import sleep

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
for i in range(len(points)):
    plot(
        [point.x for point in points[:i+1]],
        [point.y for point in points[:i+1]],
        color='b', linewidth=1.5, antialiased=True
    )
    draw()
    sleep(0.5)

show()
