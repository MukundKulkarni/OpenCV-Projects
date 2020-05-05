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

image = image[10:, 10:]

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5,5), 0)

cv2.imshow("Orignal", blurred)

canny = cv2.Canny(blurred,40, 150) # (Gradient1, Gradient2) using canny edge detection
#Any Gradient value below Gradient1 is considered not edge and vice-versa

cv2.imshow("Canny", canny)

cv2.waitKey(0)

(cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #find contours modifies the orignal image so donot use in later part of the code

print("I count {} coins.".format(len(cnts)))

coins = image.copy()

cv2.drawContours(coins, cnts, -1, (0,0,255), 2)

cv2.imshow("Coins", coins)

cv2.waitKey(0)
