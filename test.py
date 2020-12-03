import numpy as np
from PIL import Image, ImageOps, ImageFilter, ImageFont, ImageDraw
from Attacks.Manipulator import Manipulator
from PIL.ImageFilter import (
   CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

# manis = ['rotate15', {'crop':{'left':0.1, 'right':0.8,"upper":0.25,"lower":0.75}}]
manis = [{'filter':['BLUR5']}]
img = Image.open('Data/Originals/0.jpg')

m = Manipulator(manis)
img = m.apply(img)
img.save('Demo_images/rotatecrop.jpg')