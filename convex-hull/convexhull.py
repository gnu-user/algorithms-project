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
from math import sqrt

points = [[1,3], [3,2], [4,2], [-2,4], [-5,3], [2,-4], [3,-6], [-5,-9], [-4,-5]]

c =[None, None, None, None]
q = [[], [], [],[]]
w = 0
max_ca = 0;
max_cb = 0;
max_cc = 0;
max_cd = 0;
print len(points)
while(w < len(points)):
	x = points[w][0]
	y = points[w][1]
	
	# The first quadrent is origin inclusive
	# Covering elements (0, i) and (0, i) where i >= 0
	if(x >= 0 and y >= 0):
		print x, y
		d = (sqrt(points[w][0]*points[w][0] + points[w][1]*points[w][1]))
		print d
		# Store an index array of indexes of values in the first quadrent
		q[0].append(w)
		if(d >= max_ca):
			max_ca = d
			c[0] = w	
	elif(x < 0 and y > 0):
		print x, y
		d = (sqrt(points[w][0]*points[w][0] + points[w][1]*points[w][1]))
		print d
		# Store an index array of indexes of values in the second quadrent
		q[1].append(w)	
		if(d > max_cb):
			max_cb = d
			c[1] = w
	# Though the third quadrent is 0 inclusive it does not include the origin since the first quadrent already covers it.
	# The third quadrent covers (0, -i) and (-i, 0) where i > 0
	elif(x <= 0 and y <= 0 and (x != 0 or y != 0)):
		print x, y
		d = (sqrt(points[w][0]*points[w][0] + points[w][1]*points[w][1]))
		print d
		# Store an index array of indexes of values in the third quadrent
		q[2].append(w)	
		if(d > max_cc):
			max_cc = d
			c[2] = w		
	elif(x > 0 and y < 0):
		print x, y
		d = (sqrt(points[w][0]*points[w][0] + points[w][1]*points[w][1]))
		print d
		# Store an index array of indexes of values in the fourth quadrent
		q[3].append(w)	
		if(d > max_cd):
			max_cd = d
			c[3] = w

	w += 1

print c
print q

# draw a line between c[i] and c[i+1]
# recursive call starts here

m = (float)(points[c[0]][1] - points[c[1]][1])/(points[c[0]][0] - points[c[1]][0])

b = (-1) * m*(points[c[0]][0]) + points[c[0]][1]
print m, b

# Iterate through elements with needed criteria
# Since there is 4 stages:
# 1. y > given line AND y > 0
# 2. x < given line AND x < 0
# 3. y < given line AND y < 0
# 4. x > given line AND x > 0

test = m*(points[q[0][0]][0]) + b
if(points[q[0][0]][1] > test):
	c.insert(1, q[0][0])
	
# Once all of the elements that fit the given stage 
# conditions are iterated through the 

print c

# Now draw a line between c[0] and c[1] again
# repeat until above condition is false
# increment index and continue.
# once index = len(c) draw line between c[n] and c[0] 
# once a line is draw (including all elements terminate
