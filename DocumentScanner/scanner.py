from transform import  four_point_transform
import numpy as np
import cv2
import argparse as ap

ap = ap.ArgumentParser()
ap.add_argument("-i", "--image", help="Path to image")
#ap.add_argument("-c", "--coord", help="Coordinates of the rectangle")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orignal", image)

cv2.waitKey(0)

print("Enter Comma seperated co-ordinates")
pts = []
for _ in range(4):
    a,b = map(int,input().split(","))
    pts.append((a,b))


warped = four_point_transform(image,pts)

cv2.imshow("Warped", warped)

cv2.waitKey(0)
