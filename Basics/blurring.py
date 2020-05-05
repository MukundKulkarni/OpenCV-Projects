import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, help = "Path to image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("Orignal", image)

"""
1) Averging
As the name suggests, we are going to define a k × k slid-
ing window on top of our image, where k is always an odd
number. This window is going to slide from left-to-right
and from top-to-bottom. The pixel at the center of this ma-
trix (we have to use an odd number, otherwise there would
not be a true “center”) is then set to be the average of all
other pixels surrounding it. """

blurred = np.hstack([
    cv2.blur(image, (3,3)),
    cv2.blur(image, (5,5)),
    cv2.blur(image, (7,7))
])

cv2.imshow("Blurred1", blurred)

"""
Gaussian blurring is similar to average blurring, but instead of
using a simple mean, we are now using a weighted mean,
where neighborhood pixels that are closer to the central
pixel contribute more “weight” to the average."""

blurred = np.hstack([
    cv2.GaussianBlur(image, (3,3), 0),
    cv2.GaussianBlur(image, (5,5), 0),
    cv2.GaussianBlur(image, (7,7), 0),
])

cv2.imshow("Blurred2", blurred)

"""
the median blur method has been most ef-
fective when removing salt-and-pepper noise"""

blurred = np.hstack([
    cv2.medianBlur(image, 3),
    cv2.medianBlur(image, 5),
    cv2.medianBlur(image, 7),

])


cv2.imshow("Blurred3", blurred)

cv2.waitKey(0)
