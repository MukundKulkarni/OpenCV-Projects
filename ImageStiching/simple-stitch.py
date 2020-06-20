import cv2
import argparse
import  numpy as np
from os import walk
import glob

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required = True, help = "Path to the folder containg input images")
ap.add_argument("-o", "--output", required = True, help = "Path of the output image")

args = vars(ap.parse_args())

path = args["input"]

file_list = []

for filename in glob.glob(path+"/*.jpg"):
    file_list.append(filename)

file_list = sorted(file_list)
images = []

for filename in file_list:
    image = cv2.imread(filename)
    #cv2.imshow("IMG",image)
    #cv2.waitKey(0)
    images.append(image)

print("STITCHING IMAGES ")

stitcher = cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

if status == 0:
    cv2.imwrite(args["output"], stitched)
    cv2.imshow("Stitched", stitched)
    cv2.waitKey(0)
else:
    print("IMAGE STITCHING FAILED")
