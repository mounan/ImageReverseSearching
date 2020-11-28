from Approaches.ColorQuantization import get_proportion_vector
from Approaches.PHash import get_phash_vector
import cv2
import os
from PIL import Image
import timeit
import json
import imagehash
from Attacks.Manipulator import Manipulator, pil2cv, cv2pil
from Attacks.Manipulator import (
    CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
) 

class FeatureVectorConstructor:
    
    def __init__(self, dir_path:str, approach:str, tar_path=None):
        '''
        approach: 'color' or 'phash'
        attack: modifications
        '''
        super().__init__()
        self.dir = dir_path
        self.tar = tar_path
        self.apc = approach
        
        self.images = os.listdir(self.dir)
        if ".DS_Store" in self.images:
            self.images.remove(".DS_Store")

        self.vector_dict = {}
        self.time_rate = 0.0

    def construct(self):
        if self.apc == 'color':
            t1 = timeit.default_timer()
            for image in self.images:
                img = cv2.imread(f"{self.dir}/{image}")
                self.get_vector_dictvector_dict[image] = get_proportion_vector(img)
            t2 = timeit.default_timer()
            self.time_rate = (t2-t1) / len(self.images)
        elif self.apc == 'phash':
            t1 = timeit.default_timer()
            for image in self.images:
                img = Image.open(f"Data/Originals/{image}")
                self.vector_dict[image] = get_phash_vector(img)
            t2 = timeit.default_timer()
            self.time_rate = (t2-t1) / len(self.images)
            pass

    def construct_with_attack(self, attack):
        attack_approach_dict = {}
        if self.apc == 'color':
            pass
        elif self.apc == 'phash':
            for image in self.images:
                img = Image.open(f"Data/Originals/{image}")
                if attack == 'flip':
                    m = Manipulator(img)
                    m.flip()
                    a_img = m.res
                attack_approach_dict[image] = get_phash_vector(a_img)
        return attack_approach_dict

    def get_vector_dict(self):
        return self.vector_dict
    
    def get_time_rate(self):
        return self.time_rate