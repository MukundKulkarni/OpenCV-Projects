import cv2
import argparse
import  numpy as np
from os import walk
import glob
import imutils

def resize(image,y ):
    r = float(y)/image.shape[1] # Maintain the aspect ratio

    dim = (y, int(image.shape[0]*r))

    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    return resized

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
    image = resize(cv2.imread(filename), 400)
    #image = imutils.resize(cv2.imread(filename),width=400)   #IMUTILS PRESERVES THE ASPECT RATIO, YOU WON'T HAVE TO MAKE A SEPERATE FUNCTION FOR IT.
    cv2.imshow("IMG",image)
    cv2.waitKey(0)
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
