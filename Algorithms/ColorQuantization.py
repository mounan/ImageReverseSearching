import cv2
import numpy as np
import pandas as pd


def kmeans_trans(img, K=10, attempts=10, epsilon=0.1, max_iter=10, lab=False):
    '''
    img: cv2.imread('path')
    '''
    if lab is True:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    Z = np.float32(img.reshape((-1, 3)))

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, max_iter, epsilon)
    K = K
    attempts = attempts
    ret, label, center = cv2.kmeans(Z, K , None, criteria, attempts, cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    res = center[label.flatten()]
    res = res.reshape((img.shape))
    if lab is True:
        res = cv2.cvtColor(res, cv2.COLOR_LAB2BGR)
    return res, label

def proportion_list(label):
    """
    input: a label list of an image after kmeans transformation
    return: a sorted color proportion list
    """
    return (np.sort(np.unique(label, return_counts=True)[1]/len(label))*100)[::-1]    
    
def get_proportion_vector(img, K=10, attempts=10, epsilon=0.0001, max_iter=500, lab=True):
    res, label = kmeans_trans(img, K, attempts, epsilon, max_iter, lab)
    return proportion_list(label)

def dist(v1, v2):
    '''
    euclidean distance
    '''
    pass