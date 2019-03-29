#! /usr/local/bin/python2

import cv2
import numpy as np

img = cv2.imread("MyPic.png")

print img.item(150, 120, 0)

img.itemset((150, 120, 0), 255)

print img.item(150, 120, 0)
