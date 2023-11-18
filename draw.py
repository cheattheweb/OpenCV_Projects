import cv2 as cv
import numpy as np

# make a blank image using numpy array, all zeros=black
blank = np.zeros((500, 500, 3), dtype='uint8')
# print(blank)
# cv.imshow("blank", blank)

## Paint the image a  certain color
# blank[:] = 0, 255, 0 # colors all the pixels
# blank[200:300, 200:300] = 0, 200, 0
# cv.imshow("Green", blank)

## Draw a Rectangle
# cv.rectangle(blank, (0,0), (300, 300), (0,150,0), thickness=cv.FILLED)
# cv.rectangle(blank, (0,0), (blank.shape[1] // 2, blank.shape[0] // 2), (0,150,0), thickness=cv.FILLED)

## Draw a Circle
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 50, (0, 100, 0), thickness=cv.FILLED)

## Draw a line
cv.line(blank, (100, 150), (blank.shape[1] // 2, blank.shape[0] // 2), (255, 255, 0))

cv.imshow("Page", blank)
## Write text on a image
cv.putText(blank, "Hello World", (blank.shape[1] // 2, blank.shape[0] // 2), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0),
           thickness=2)
cv.imshow("Text", blank)

## triangle
print(blank)
cv.waitKey(0)
