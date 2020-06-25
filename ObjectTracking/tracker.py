import cv2
import argparse
import numpy as np
import  time

OPENCV_OBJECT_TRACKERS = {
	"csrt": cv2.TrackerCSRT_create,
	"kcf": cv2.TrackerKCF_create,
	"boosting": cv2.TrackerBoosting_create,
	"mil": cv2.TrackerMIL_create,
	"tld": cv2.TrackerTLD_create,
	"medianflow": cv2.TrackerMedianFlow_create,
	"mosse": cv2.TrackerMOSSE_create
}

def resize(image,y ):
    r = float(y)/image.shape[1] # Maintain the aspect ratio
    dim = (y, int(image.shape[0]*r))
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    return resized

ap = argparse.ArgumentParser()

ap.add_argument("-v", "--video",required = False, default = 0, help="Path to input video")
ap.add_argument("-t", "--tracker", required = False, default = "kcf", help = "Tracking algorithm to use")

args = vars(ap.parse_args())

tracker = OPENCV_OBJECT_TRACKERS[args["tracker"]]()

init_BB = None
success = False

vs = cv2.VideoCapture(0)
vs.set(cv2.CAP_PROP_FPS, 10)
time.sleep(2.0)

while True:

    ret, frame = vs.read()

    if frame is None:
        break

    (H, W) = frame.shape[:2]

    if init_BB is not None:
        (success, box) = tracker.update(frame)
    #else:
        #init_BB = cv2.selectROI("Frame", frame, fromCenter = False, showCrosshair = True)
        #tracker.init(frame, init_BB)


    if success:
        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h),
        (0, 255, 0), 2)


    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        init_BB = cv2.selectROI("Frame", frame, fromCenter = False, showCrosshair = True)
        tracker.init(frame, init_BB)

    elif key == ord('q'):
        break

vs.release()
cv2.destroyAllWindows()
