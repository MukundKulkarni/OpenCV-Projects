import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, help = "Path to image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("Orignal", image)

chan = cv2.split(image)
colors = ("b", "g", "r")




plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan, color) in zip(chan, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0,256])
    plt.plot(hist, color = color)
    plt.xlim([0,256])

plt.show()

cv2.waitKey(0)
