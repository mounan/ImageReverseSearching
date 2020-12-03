import numpy as np
from PIL import Image, ImageOps, ImageFilter, ImageFont, ImageDraw
from PIL.ImageFilter import (
   CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)


class Manipulator:
    '''
    manipulations: list
    ["flip","mirror",'rotate(deg)',
        {'crop':{"left":float,"upper":float,"right":float,"lower":float}},
        'scale(ratio)', 'grayscale',{'filter':['BLUR(num)', CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN]}]
    '''
    def __init__(self, manipulations):
        self.manipulations = manipulations
    
    def apply(self, img):
        for mani in self.manipulations:
            if "flip" == mani:
                img = ImageOps.flip(img) 
            elif "mirror" == mani:
                img = ImageOps.mirror(img)
            elif 'rotate' in mani:
                degree = int(mani[6:])
                # if degree % 90 == 0:
                #     img = img.rotate(degree, expand=True)
                # else:
                #     img = img.rotate(degree, expand=False)
                img = img.rotate(degree, expand=True)
            elif 'crop' in mani:
                width, height = img.size
                img = img.crop((mani['crop']['left']*width, mani['crop']['upper']*height, mani['crop']['right']*width, mani['crop']['lower']*height))
            elif "scale" in mani and 'gray' not in mani:
                ratio = float(mani[5:])
                width = img.width
                height = img.height  
                img = img.resize((int(ratio*width), int(ratio*height)))
            elif 'grayscale' == mani:  
                gamma22LUT  = [pow(x/255.0, 2.2)*255 for x in range(256)] * 3
                gamma045LUT = [pow(x/255.0, 1.0/2.2)*255 for x in range(256)]
                img_rgb = img.convert("RGB")
                img_rgbL = img_rgb.point(gamma22LUT)
                img_grayL = img_rgbL.convert("L")  # RGB to L(grayscale)
                img_gray = img_grayL.point(gamma045LUT)
                img = img_gray
            elif 'filter' in mani:
                img = self.add_filter(img, mani['filter'])
            elif 'watermark' in mani:
                width = img.width
                height = img.height
                font = ImageFont.truetype("Attacks/times-ro.ttf", width//20)
                draw = ImageDraw.Draw(img)
                draw.text((width/2, height/2),"Sample Water Mark",(255,255,255),font=font)
        return img

    def add_filter(self, img, filters): # pil_img
        """
        filters: "BULR(num)", CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
        EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
        """
        for filter in filters:
            if type(filter) is str:
                if "BLUR" in filter:
                    img = img.filter(ImageFilter.GaussianBlur(int(filter[4:])))
            else:
                img = img.filter(filter)
        return img
    
    




    


        

