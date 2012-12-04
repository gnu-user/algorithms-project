from matplotlib.pyplot import *
import matplotlib.lines
import matplotlib.image as mpimg
import numpy as np


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


#import FigureCanvasQTAgg as FigureCanvas

#picture = Image.open('toronto_map.png')
img = imread('toronto_map_points.png')
imgplot = imshow(img)
#CSbkgr = self.axes.imshow(picture, origin='lower')

axis([0, 653, 429, 0])
title('Shortest Path')
#grid(True)

#user_points = ginput(n=0,timeout=0, show_clicks=True)
#for point in user_points:
#    map(float, point)
#    print(point)


# Dictionary mapping points to the Vector
points = {	'A': Vector(70.471215880893297, 423.99702233250616),
			'B': Vector(114.54466501240695, 411.03424317617862),
			'C': Vector(161.21066997518614, 396.77518610421834),
			'D': Vector(208.86458333333331, 383.27083333333326),
			'E': Vector(263.70833333333326, 364.98958333333326),
			'F': Vector(280.63541666666663, 415.77083333333326),
			'G': Vector(333.44791666666663, 400.19791666666657),
			'H': Vector(357.82291666666663, 391.39583333333326),
			'I': Vector(385.58333333333326, 382.59374999999989),
			'J': Vector(363.91666666666663, 310.82291666666663),
			'K': Vector(336.15624999999989, 229.57291666666663),
			'L': Vector(288.76041666666663, 245.82291666666663),
			'M': Vector(229.17708333333326, 262.07291666666663),
			'N': Vector(179.07291666666663, 278.99999999999994),
			'O': Vector(127.61458333333331, 295.24999999999994),
			'P': Vector(82.927083333333314, 311.49999999999994),
			'Q': Vector(37.5625, 324.36458333333326),
			'R': Vector(20.635416666666686, 268.84374999999994),
			'S': Vector(5.7395833333333428, 216.03124999999994),
			'T': Vector(62.614583333333314, 138.16666666666663),
			'U': Vector(322.61458333333326, 178.79166666666663),
			'V': Vector(367.97916666666663, 164.57291666666663),
			'W': Vector(161.46874999999994, 54.208333333333314),
			'X': Vector(172.97916666666663, 103.63541666666663),
			'Y': Vector(187.19791666666663, 155.09375),
			'Z': Vector(204.80208333333331, 211.29166666666663),
			'1': Vector(355.11458333333326, 105.66666666666663),
			'2': Vector(336.15624999999989, 56.916666666666686),
			'3': Vector(321.26041666666663, 8.84375)
}



# A sample graph containing the shortest path
shotest_path = ['C', 'D']

print("SHORTEST PATH:")
print(shotest_path)

for point in shotest_path:
    print(points[point].x, points[point].y)

# Plot the points 
plot([points[point].x for point in shotest_path],
    [points[point].y for point in shotest_path],
    linewidth=5, antialiased=True)

#draw()
#        sleep(0.5)
#    del hull[-1]

show()