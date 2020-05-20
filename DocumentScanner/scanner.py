from transform import  four_point_transform
import numpy as np
import cv2
import argparse as ap
from matplotlib import  pyplot as plt
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

r = 400.0/image.shape[1]

dim = (400, int(image.shape[0]*r))

image = cv2.resize(image,dim, interpolation = cv2.INTER_AREA)
image = image[140:510, 0:400]
cv2.imshow("Orignal", image)
cv2.namedWindow('image')


cv2.setMouseCallback('image',get_points)
while True:
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

print(pts)

pts2 = np.float32([[0,0],[300,0],[300,300],[0,300]])
pts1 =np.float32(pts)

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(image,M,(300,300))

plt.subplot(121),plt.imshow(image),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

cv2.waitKey(0)
