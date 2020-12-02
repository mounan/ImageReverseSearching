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

data_path = 'Data/Originals'
# manis = ["flip", "mirror", "rotate90", "scale2", "grayscale", {"filter":['BLUR20',CONTOUR, DETAIL, EDGE_ENHANCE]}]
manis = ['flip']

color_fvc = FVC(dir_path=data_path, algorithm='color')
original_color_feature_vectors = color_fvc.construct()
mani_color_feature_vectors = color_fvc.construct_with_manipulation(manis)
color_acc = match_acc(base=original_color_feature_vectors, queries=mani_color_feature_vectors, dist="euclidean")
print(color_acc)
# phash_fvc = FVC(dir_path=data_path, algorithm='phash')
# original_phash_feature_vectors = phash_fvc.construct()
# mani_phash_feature_vectors = phash_fvc.construct_with_manipulation(manis)
# phash_acc = match_acc(base=original_phash_feature_vectors, queries=mani_phash_feature_vectors, dist="hamming")
# print(phash_acc)

















