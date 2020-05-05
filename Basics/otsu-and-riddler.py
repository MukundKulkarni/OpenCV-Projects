import numpy as np
import mahotas
import argparse
import cv2


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

T = mahotas.thresholding.otsu(blurred)

print("Otsu Threshold {}".format(T))

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0

cv2.imshow("Otsu", thresh)

thresh = image.copy()
T = mahotas.thresholding.rc(blurred)
print("Riddler - Calavard THRESHOLD {}".format(T))

thresh[thresh > T] = 255
thresh[thresh < T] = 0

cv2.imshow("Riddler - Calavard", thresh)

cv2.waitKey(0)
