from PIL import Image
from Algorithms.ColorQuantization import kmeans_trans
import Algorithms.PHash as phash
from FeatureVectorConstructor import FeatureVectorConstructor as FVC
from Attacks.Manipulator import Manipulator
from PIL.ImageFilter import (
   CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)
from Analyzers.accuracy import match_acc
import cv2
import os
import numpy as np
import json

data_path = 'Data/Images'

color_fvc = FVC(dir_path=data_path, algorithm='color')
original_color_feature_vectors = color_fvc.construct()
np.save('Data/original_feature_vectors/color.npy',original_color_feature_vectors)

phash_fvc = FVC(dir_path=data_path, algorithm='phash')
original_phash_feature_vectors = phash_fvc.construct()
np.save('Data/original_feature_vectors/phash.npy',original_phash_feature_vectors)

time_dict = {'Construction_time_color':color_fvc.get_time_rate(),
             'Construction_time_phash':phash_fvc.get_time_rate()}
with open('exp_res.json', 'w') as f:
    json.dump(time_dict, f)
