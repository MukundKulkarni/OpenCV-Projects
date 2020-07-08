import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(3)

for _ in range(60):
    ret, background = cap.read()
    flipped = cv2.flip(background, 1)
    cv2.imshow("background", flipped)

cv2.imwrite("background.jpg", flipped)
cv2.waitKey(0)
