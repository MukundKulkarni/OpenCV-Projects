import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, help = "Path to image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orignal", image)

(h,w) = image.shape[0],image.shape[1]
center = (w//2,h//2)

M = cv2.getRotationMatrix2D( center,45, 1.0)

rotated = cv2.warpAffine(image, M, (w,h))

cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
