import numpy as np
import  argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to imput image")
ap.add_argument("-p", "--protxt", required = True, help = "Path to caffe \"deploy\" protxt file")
ap.add_argument("-m", "--model", required = True, help = "Path to caffe pre-trained model")
ap.add_argument("-c", "--confidence", required = True, type=float, default = 0.5, help = "Minimum probablity to filter weak detections")

args = vars(ap.parse_args())
