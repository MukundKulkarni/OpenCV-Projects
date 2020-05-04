import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, help = "Path to image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orignal", image)
#A color image consists of multiple channels: a Red, a Green,and a Blue component.
(B,G,R) = cv2.split(image)

cv2.imshow("RED", R)
cv2.imshow("GREEN", G)
cv2.imshow("BLUE", B)

cv2.waitKey(0)
