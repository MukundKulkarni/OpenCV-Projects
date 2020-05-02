import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, help = "Path to image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orignal", image)

r = 1250.0/image.shape[1] # Maintain the aspect ratio

dim = (1250, int(image.shape[0]*r))

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) # INTER_LINER, _CUBIC, _NEAREST CAN also be used

cv2.imshow("Resized", resized)

cv2.waitKey(0)
