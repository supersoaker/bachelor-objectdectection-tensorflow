import numpy as np
import cv2
import sys
import matplotlib.pyplot as plt
sys.path.insert(0, './google-data/DataAugmentationForObjectDetection')
from DataAugmentationForObjectDetection.data_aug.data_aug import *
from DataAugmentationForObjectDetection.data_aug.bbox_util import *
import pickle as pkl
#%matplotlib inline

def randomHorizontalFlip(img, bboxes):
    img2 = img.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img_, bboxes_ = RandomHorizontalFlip(1)(img2, bboxes.copy())
    plotted_img = draw_rect(img_, bboxes_, (66, 244, 104))
    return plotted_img

def randomScale(img, bboxes):
    img2 = img.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img_, bboxes_ = RandomScale(0.3, diff=True)(img2, bboxes.copy())
    plotted_img = draw_rect(img_, bboxes_, (66, 244, 104))
    return plotted_img

def randomTranslate(img, bboxes):
    img2 = img.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img_, bboxes_ = RandomTranslate(0.3, diff=True)(img2, bboxes.copy())
    plotted_img = draw_rect(img_, bboxes_, (66, 244, 104))
    return plotted_img

def randomRotate(img, bboxes):
    img2 = img.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img_, bboxes_ = RandomRotate(20)(img2, bboxes.copy())
    plotted_img = draw_rect(img_, bboxes_, (66, 244, 104))
    return plotted_img

def randomHSV(img, bboxes):
    img2 = img.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img_, bboxes_ = RandomHSV(100, 100, 100)(img2, bboxes.copy())
    plotted_img = draw_rect(img_, bboxes_, (66, 244, 104))
    return plotted_img

def randomShear(img, bboxes):
    img2 = img.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img_, bboxes_ = RandomShear(0.2)(img2, bboxes.copy())
    plotted_img = draw_rect(img_, bboxes_, (66, 244, 104))
    return plotted_img

