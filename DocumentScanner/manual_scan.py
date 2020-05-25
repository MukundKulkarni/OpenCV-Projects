from transform import  four_point_transform
import numpy as np
import cv2
import argparse as ap
from matplotlib import  pyplot as plt
from skimage.filters import threshold_local
import mahotas

pts = []
click_cnt = 0

def get_points(event,x,y,flags,param):
	global pts, click_cnt
	if event == cv2.EVENT_LBUTTONDOWN and click_cnt < 4:
		click_cnt += 1
		cv2.circle(image,(x,y),4,(0,255,0),-1)
		print(x,y)
		pts.append([x,y])



ap = ap.ArgumentParser()
ap.add_argument("-i", "--image", help="Path to image")
#ap.add_argument("-c", "--coord", help="Coordinates of the rectangle")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

r = 600.0/image.shape[1]

dim = (600, int(image.shape[0]*r))

image = cv2.resize(image,dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Orignal", image)
cv2.namedWindow('image')


cv2.setMouseCallback('image',get_points)
while True:
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

print(pts)
pts1 =np.float32(pts)

width = max(pts1[1][0] - pts1[0][0], pts1[2][0] - pts1[3][0])
height = max(pts1[3][1] - pts1[0][1], pts1[2][1] - pts1[1][1])

pts2 = np.float32([[0,0],[width,0],[width,height],[0,height]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(image,M,(width,height))

warped = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset = 10, method = "gaussian")
warped = (warped > T).astype("uint8") * 255

cv2.imshow("Original", image)
cv2.imshow("Scanned", warped)
cv2.waitKey(0)
