from matplotlib.pyplot import *
import matplotlib.lines
import matplotlib.image as mpimg
import numpy as np
#import FigureCanvasQTAgg as FigureCanvas

#picture = Image.open('toronto_map.png')
img = imread('toronto_map.png')
imgplot = imshow(img)
#CSbkgr = self.axes.imshow(picture, origin='lower')

#axis([0, 10, 0, 10])
#title('Convex Hull')
#grid(True)

user_points = ginput(n=0,timeout=0, show_clicks=True)
for point in user_points:
    map(float, point)
    print(point)

show()