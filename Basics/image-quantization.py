from sklearn.cluster import MiniBatchKMeans
import argparse
import cv2
import numpy as np

def resize(image,y ):
    r = float(y)/image.shape[1] # Maintain the aspect ratio

    dim = (y, int(image.shape[0]*r))

    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    return resized

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help = "path to image")
ap.add_argument("-o", "--output", required = False, help = "path of output image")
ap.add_argument("-c", "--clusters", required = True, type = int, help = "number of clusters")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = resize(image, 800)
(h,w) = image.shape[:2]

image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

image = image.reshape(image.shape[0] * image.shape[1], 3)


clt = MiniBatchKMeans(n_clusters = args["clusters"])
labels = clt.fit_predict(image)
quant = clt.cluster_centers_.astype("uint8")[labels]

quant = quant.reshape((h, w, 3))
image = image.reshape((h, w, 3))

quant = cv2.cvtColor(quant, cv2.COLOR_LAB2BGR)
image = cv2.cvtColor(image, cv2.COLOR_LAB2BGR)


cv2.imshow("Image",np.hstack([image, quant]))

cv2.waitKey(0)
