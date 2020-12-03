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


