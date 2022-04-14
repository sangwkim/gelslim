#!/usr/bin/env python

import numpy as np
import math, os, cv2
from PIL import Image
import matplotlib.pyplot as plt

ab_array = np.load('abe_corr.npz')
x_index = ab_array['x']
y_index = ab_array['y']

img = cv2.imread('g2_28.jpg')
img = img[x_index, y_index, :]
plt.imshow(img)
plt.show()
input()



"""
from PIL import Image
import glob, os

import re
def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

# Create the frames
frames = []
imgs = sorted(glob.glob(f'{os.getcwd()}/*.png'), key=numericalSort)
#imgs = glob.glob("plot_*.png")
for i in imgs:
    new_frame = Image.open(i)
    width, height = new_frame.size
    #frames.append(new_frame)
    #frames.append(new_frame.resize((250,250)))
    frames.append(new_frame.crop((0.13*width,0.13*height,0.89*width,0.89*height)).resize((300,300)))

# Save into a GIF file that loops forever
frames[0].save('png_to_gif.gif', format='GIF',
               append_images=frames[400::2],
               save_all=True,
               duration=80, loop=0)
"""