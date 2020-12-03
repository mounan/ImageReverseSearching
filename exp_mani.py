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
from database_constructor import data_path
from test import manis
# manis = ['grayscale']

color_fvc = FVC(dir_path=data_path, algorithm='color')
original_color_feature_vectors = np.load('Data/original_feature_vectors/color.npy',allow_pickle=True)[()] # convert ndarray to dict

mani_color_feature_vectors = color_fvc.construct_with_manipulation(manis)
color_acc = match_acc(base=original_color_feature_vectors, queries=mani_color_feature_vectors, dist="euclidean")

phash_fvc = FVC(dir_path=data_path, algorithm='phash')
original_phash_feature_vectors = np.load('Data/original_feature_vectors/phash.npy',allow_pickle=True)[()]
mani_phash_feature_vectors = phash_fvc.construct_with_manipulation(manis)
phash_acc = match_acc(base=original_phash_feature_vectors, queries=mani_phash_feature_vectors, dist="hamming")

# exp_res = {
#            'manipulations':manis,
#            'color_acc':color_acc,
#            'phash_acc':phash_acc,
#           }

# with open('exp_res.json', 'a') as f:
#     json.dump(exp_res, f, indent=2)

print(color_acc)
print(phash_acc)
















