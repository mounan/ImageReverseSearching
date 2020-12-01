from algorithmes.ColorQuantization import get_proportion_vector
from algorithmes.PHash import get_phash_vector
import cv2
import os
from PIL import Image
import timeit
import json
import imagehash
from manipulations.Manipulator import Manipulator, pil2cv, cv2pil
from manipulations.Manipulator import (
    CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
) 

class FeatureVectorConstructor:
    
    def __init__(self, dir_path:str, algorithm:str, tar_path=None):
        '''
        algorithm: 'color' or 'phash'
        manipulation: modifications
        '''    
        super().__init__()
        self.dir = dir_path
        self.tar = tar_path
        self.apc = algorithm

        self.images = os.listdir(self.dir)
        if ".DS_Store" in self.images:
            self.images.remove(".DS_Store")

        self.original_vector_dict = {}
        self.manipulated_vector_dict = {}
        self.time_rate = 0.0

    def construct(self):
        if self.apc == 'color':
            t1 = timeit.default_timer()
            for image in self.images:
                img = cv2.imread(f"{self.dir}/{image}")
                self.original_vector_dict[image] = get_proportion_vector(img)
            t2 = timeit.default_timer()
            self.time_rate = (t2-t1) / len(self.images)
        elif self.apc == 'phash':
            t1 = timeit.default_timer()
            for image in self.images:
                img = Image.open(f"Data/Originals/{image}")
                self.original_vector_dict[image] = get_phash_vector(img)
            t2 = timeit.default_timer()
            self.time_rate = (t2-t1) / len(self.images)
        return self.original_vector_dict

    def construct_with_manipulation(self, manipulations):
        m = Manipulator(manipulations)
        if self.apc == 'color':
            pass
        elif self.apc == 'phash':
            for image in self.images:
                img = Image.open(f"Data/Originals/{image}")
                m_img = m.apply(img)
                self.manipulated_vector_dict[image] = get_phash_vector(m_img)
        return self.manipulated_vector_dict

    def get_original_vector_dict(self):
        return self.original_vector_dict
    
    def get_time_rate(self):
        return self.time_rate