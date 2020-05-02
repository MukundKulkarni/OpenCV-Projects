import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, help = "Path to image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orignal", image)

M = np.float32([[1,0,25],[0,1,50]]) # Transformation matrix [1,0,tx],[0,1,ty]

shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Shifted", shifted)

cv2.waitKey(0)
