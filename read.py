import cv2 as cv

# Reading Images
# img = cv.imread("Photos/cat.jpg")
# cv.imshow("Cat", img)

# cv.waitKey(0)

# Reading Videos
# capture = cv.VideoCapture(0) # 0 is the default webcam
capture = cv.VideoCapture("Videos/dog.mp4")

while True:  # While the video is playing
    isTrue, frame = capture.read()  # isTrue is a boolean value that tells us if the video is playing or not
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord("d"):  # If the letter d is pressed, the video will stop
        break

capture.release()  # Release the capture

quit()
