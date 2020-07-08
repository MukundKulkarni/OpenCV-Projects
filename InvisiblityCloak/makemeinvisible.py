import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(1)

background = cv2.imread("background.jpg")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    flipped = cv2.flip(frame, 1)
    # Display the resulting frame

    hsv = cv2.cvtColor(flipped, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 125, 50])
    upper_red = np.array([10, 255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask = mask1 + mask2

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))

    mask2 = cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(flipped, flipped, mask = mask2)

    res2 = cv2.bitwise_and(background, background, mask = mask1)
    finalOutput = cv2.addWeighted(res1, 1, res2, 1, 0)


    cv2.imshow('flipped',finalOutput)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
