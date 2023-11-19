# we have to import opencv
import cv2 as cv

# in this file we will take an image and show it, as well
# a video too

# 1. Reading Image
# use the imread() to take input and store its array in image
img = cv.imread("Photos/cats.jpg")
# show the image using imshow()
cv.imshow("Cats", img)
# cv.waitKey(0)

# 2. Reading Videos
# 1st we have to include a source in a variable
capture = cv.VideoCapture("Videos/kitten.mp4")  # for camera use 0,1..

# for video we have to make a while loop
while True:

    isTrue, frame = capture.read()  # isTrue will tell us if there is video or not
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xff == ord("s"):
        # if i pass 0 it waits for each frame a key to be press
        # if cv.waitKey(0) & off==ord('s'):
        break
