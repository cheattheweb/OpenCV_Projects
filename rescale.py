import cv2 as cv

# rescale the video or photo
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("Photos/cat_large.jpg")
cv.imshow("Cat",rescaleFrame(img, 0.3))

capture = cv.VideoCapture("Videos/dog.mp4")

while True:  # While the video is playing
    isTrue, frame = capture.read()  # isTrue is a boolean value that tells us if the video is playing or not

    frame_resized = rescaleFrame(frame)

    cv.imshow("Resized Video", frame_resized)
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord("d"):  # If the letter d is pressed, the video will stop
        break

capture.release()  # Release the capture
