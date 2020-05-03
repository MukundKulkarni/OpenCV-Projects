import cv2
import numpy as np


rectangle = np.zeros((300,300), dtype = "uint8")

cv2.rectangle(rectangle, (25,25), (275,275), 255, -1)

cv2.imshow("rectangle", rectangle)


circle = np.zeros((300,300), dtype = "uint8")

cv2.circle(circle, (circle.shape[0]//2, circle.shape[1]//2), 150, 255, -1)

cv2.imshow("circle", circle)


bitwiseAND = cv2.bitwise_and(rectangle,circle)
cv2.imshow("AND", bitwiseAND)

bitwiseOR = cv2.bitwise_or(rectangle,circle)
cv2.imshow("OR", bitwiseOR)

bitwiseXOR = cv2.bitwise_xor(rectangle,circle)
cv2.imshow("XOR", bitwiseXOR)

bitwiseNOT = cv2.bitwise_not(rectangle,circle)
cv2.imshow("NOT", bitwiseNOT)




cv2.waitKey(0)
