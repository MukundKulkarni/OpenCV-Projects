import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, help = "Path to image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orignal", image)

flipped = cv2.flip(image, 1) # use 0 to filp horizontally , -1 fot both

cv2.imshow("Flipped", flipped)

cv2.waitKey(0)
