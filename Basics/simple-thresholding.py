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

(T, thresh) = cv2.threshold(blurred, 140, 255, cv2.THRESH_BINARY) # We manually supply the threshold value, every pixel have value greater than 140 is set to 255

cv2.imshow("Binary Thresholding", thresh)

(T, thresh) = cv2.threshold(blurred, 140, 255, cv2.THRESH_BINARY_INV) # We manually supply the threshold value, every pixel have value greater than 140 is set to 255

cv2.imshow("Inverse Binary Thresholding", thresh)




cv2.waitKey(0)
