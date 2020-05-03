import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, help = "Path to image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orignal", image)


mask1 = np.zeros(image.shape[:2], dtype = "uint8")
(cx, cy) = (image.shape[1]//2 , image.shape[0]//2)

cv2.rectangle(mask1, (cx - 75, cy - 75), (cx + 75, cy + 75), 255, -1)
cv2.imshow("Mask1", mask1)

masked1 = cv2.bitwise_and(image, image, mask = mask1) # using the mask attribute limits the computation only to the mask

cv2.imshow("Masked1", masked1)

mask2 = np.zeros(image.shape[:2], dtype = "uint8")
(cx, cy) = (image.shape[1]//2 , image.shape[0]//2)


cv2.circle(mask2, (cx, cy), 125, 255, -1)
cv2.imshow("Mask2", mask2)

masked2 = cv2.bitwise_and(image, image, mask = mask2) # using the mask attribute limits the computation only to the mask

cv2.imshow("Masked2", masked2)



cv2.waitKey(0)
