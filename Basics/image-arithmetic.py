import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, help = "Path to image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orignal", image)

M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M) # cv2.add clips the value if value goes beyond 255 whereas np.add rotates the value
cv2.imshow("Added", added)

M = np.ones(image.shape, dtype = "uint8") * 50
subtract = cv2.subtract(image, M) # cv2.subtract clips the value if value goes beyond 0 whereas np.add rotates the value
cv2.imshow("Subtract", subtract)



cv2.waitKey(0)
