from typing import Any

import cv2 as cv
from cv2 import Mat
from numpy import ndarray, dtype, generic


# rescale a video or photo
def rescaleframe(frame, scale=0.7):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread("Photos/cat_large.jpg")
cv.imshow("Cat", rescaleframe(img))
cv.waitKey(0)

capture = cv.VideoCapture("Videos/dog.mp4")

# for video
while True:
    isTrue, frame = capture.read()

    cv.imshow("Dog Video", rescaleframe(frame))

    if cv.waitKey(6) & 0xFF == ord("s"):
        break


capture.release()  # release the captured video
# for pic



quit()
