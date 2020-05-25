from transform import  four_point_transform
import numpy as np
import cv2
import argparse as ap
from matplotlib import  pyplot as plt
from skimage.filters import threshold_local
import mahotas
import imutils


ap = ap.ArgumentParser()
ap.add_argument("-i", "--image", help="Path to image")
#ap.add_argument("-c", "--coord", help="Coordinates of the rectangle")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

r = 600.0/image.shape[1]

dim = (600, int(image.shape[0]*r))

image = cv2.resize(image,dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Orignal", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray,(5,5),0)

edged = cv2.Canny(blurred, 75, 200)

cv2.imshow("Canny", edged)


cv2.waitKey(0)

cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
# loop over the contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	# if our approximated contour has four points, then we
	# can assume that we have found our screen
	if len(approx) == 4:
		screenCnt = approx
		break
# show the contour (outline) of the piece of paper
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.imshow("Outline", image)
cv2.waitKey(0)


warped = four_point_transform(image, screenCnt.reshape(4,2))

warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset = 10, method = "gaussian")
warped = (warped > T).astype("uint8") * 255
# show the original and scanned images
print("STEP 3: Apply perspective transform")
cv2.imshow("Original", imutils.resize(image, height = 650))
cv2.imshow("Scanned", imutils.resize(warped, height = 650))
cv2.waitKey(0)
