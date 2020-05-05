import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, help = "Path to image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

#The image is too large, so resize it

r = 400.0/image.shape[1]

dim = (400, int(image.shape[0]*r))

image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(image, (5,5), 0)

cv2.imshow("Orignal", blurred)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 9)
# (IMAGE, SET-PIXLE-COLOR, ADAPTIVE_THRESH_MEAN_C USING MEAN, BINARY THRESH, SIZE OF KERNEL, CONSTANT TO FINE TUNE OUR THRESHOLD )
cv2.imshow("MEAN THRESH", thresh)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 9)
# (IMAGE, SET-PIXLE-COLOR, ADAPTIVE_THRESH_GAUSSIAN_C USING GAUSSIAN MEAN, BINARY THRESH, SIZE OF KERNEL, CONSTANT TO FINE TUNE OUR THRESHOLD )
cv2.imshow("GAUSSIAN THRESH", thresh)




cv2.waitKey(0)
