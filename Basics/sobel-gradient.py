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

cv2.imshow("Orignal", image)

sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

sobelcombined = cv2.bitwise_or(sobelx, sobely)

cv2.imshow("SobelX", sobelx)
cv2.imshow("SobelY", sobely)
cv2.imshow("Sobel combined", sobelcombined)


cv2.waitKey(0)
