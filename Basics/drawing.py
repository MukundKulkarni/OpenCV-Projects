import cv2
import numpy as np

canvas = np.zeros((300,300,3), dtype = "uint8")

(centerx,centery) = canvas.shape[1]//2, canvas.shape[0]//2
white = (255,255,255) # Remeber color scheme is BGR not RGB

for radius in range(0,175,25):
    cv2.circle(canvas, (centerx,centery), radius, white,3)

cv2.imshow("Bull's Eye", canvas)

cv2.waitKey(0)
