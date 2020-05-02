import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, help = "Path to image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orignal", image)

cropped = image[50:200, 50:200]
cv2.imshow("Cropped", cropped)

cv2.waitKey(0)
