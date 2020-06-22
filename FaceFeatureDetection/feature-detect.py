import cv2
import  numpy as np
import  dlib
import  argparse
import time

def resize(image,y ):
    r = float(y)/image.shape[1] # Maintain the aspect ratio
    dim = (y, int(image.shape[0]*r))
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return resized

def shape_to_np(shape, dtype="int"):
	# initialize the list of (x, y)-coordinates
	coords = np.zeros((shape.num_parts, 2), dtype=dtype)

	# loop over all facial landmarks and convert them
	# to a 2-tuple of (x, y)-coordinates
	for i in range(0, shape.num_parts):
		coords[i] = (shape.part(i).x, shape.part(i).y)

	# return the list of (x, y)-coordinates
	return coords


ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape_predictor", required=True, help = "Path to facial landmark predictor")

args = vars(ap.parse_args())

print("[INFO] loading facial landmark detector")

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    frame = cv2.flip(frame, 1)
    #frame = resize(frame, 400)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)

    for rect in rects:
        # determine the facial landmarks for the face region, then
		# convert the facial landmark (x, y)-coordinates to a NumPy
		# array
        shape = predictor(gray, rect)
        shape = shape_to_np(shape)

        for (x,y) in shape:
            cv2.circle(frame,(x,y), 1, (0,255,0), -1)

    # Display the resulting frame

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
