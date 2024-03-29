import numpy as np
import  argparse
import cv2
import time

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--protxt", required = True, help = "Path to caffe \"deploy\" protxt file")
ap.add_argument("-m", "--model", required = True, help = "Path to caffe pre-trained model")
ap.add_argument("-c", "--confidence", required = False, type=float, default = 0.5, help = "Minimum probablity to filter weak detections")

args = vars(ap.parse_args())





# Read Model

net = cv2.dnn.readNetFromCaffe(args["protxt"], args["model"])

# load the input channel and construct an input blob for the image
# by resizing to a fixed 300x300 pixels and then normalizing it

vs = cv2.VideoCapture(0)
time.sleep(2.0)

while True:
    ret, frame = vs.read()
    (h,w) = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,(300, 300), (104.0, 177.0, 123.0))

    net.setInput(blob)

    detections = net.forward()

    for i in range(0,detections.shape[2]):

        confidence = detections[0,0,i,2]

        if confidence < args["confidence"]:
            continue

        box = detections[0,0,i,3:7] * np.array([w,h,w,h])
        (startX, startY, endX, endY) = box.astype(int)

        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

        cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0,255,0), 2)

    cv2.imshow("Image", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break


cv2.destroyAllWindows()
