import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, help = "Path to image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orignal", image)

corner = image[0:100,0:100] # get image for corner

cv2.imshow("Corner",corner)

image[0:100,0:100] = (0,0,0)

cv2.imshow("Blacked", image)


cv2.waitKey(0)
