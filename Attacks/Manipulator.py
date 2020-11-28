import cv2
import numpy as np
from PIL import Image, ImageOps, ImageFilter
from PIL.ImageFilter import (
   CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)


class Manipulator:
    def __init__(self, original):
        '''
        PIL.Image.open('path')
        '''
        self.original = original
        self.res = original # pil_img
        
    def flip(self, flipcode=0): # pil_img
        if flipcode != 0:
            self.res = ImageOps.flip(self.res) 
        else:
            self.res = ImageOps.mirror(self.res)

    def rotate(self, degree=0): # pil_img
        if degree % 90 == 0:
            self.res = self.res.rotate(degree, expand=True)
        else:
            self.res = self.res.rotate(degree, expand=False)

    def add_filter(self, *filters): # pil_img
        """
        filters: "BULR(num)", CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
        EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
        """
        for filter in filters:
            if type(filter) is str:
                if "BLUR" in filter:
                    self.res = self.res.filter(ImageFilter.GaussianBlur(int(filter[4:])))
            else:
                self.res = self.res.filter(filter)

    def crop(self, left, upper, right, lower): # pil_img
        """
        Left, upper, right, lower all refer to percentage of width and height and should be in range [0, 1].
        The top left coordinates correspond to (x, y) = (left, upper), and the bottom right coordinates correspond to (x, y) = (right, lower). The area to be cropped is left <= x <right and upper <= y <lower, and the pixels of x = right andy = lower are not included.
        """
        width, height = self.res.size
        self.res = self.res.crop((left*width, upper*height, right*width, lower*height))
    

    def scale(self, ratio): # pil_img
        width = self.res.width
        height = self.res.height
        self.res = self.res.resize((int(ratio*width), int(ratio*height)))
    
    def grayscale(self): # pil_img
        gamma22LUT  = [pow(x/255.0, 2.2)*255 for x in range(256)] * 3
        gamma045LUT = [pow(x/255.0, 1.0/2.2)*255 for x in range(256)]
        img_rgb = self.res.convert("RGB")
        img_rgbL = img_rgb.point(gamma22LUT)
        img_grayL = img_rgbL.convert("L")  # RGB to L(grayscale)
        img_gray = img_grayL.point(gamma045LUT)
        self.res = img_gray

def pil2cv(pil_img):
    return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

def cv2pil(cv_img):
    return Image.fromarray(cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB))



    


        

