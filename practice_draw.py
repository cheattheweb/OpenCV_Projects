import cv2 as cv
import numpy as np

# blanks page = all zero numpy array
blank = np.zeros((600, 600, 3), dtype='uint8')

# print will show an array
print(blank)

# imshow() will show a blank page, as an image
cv.imshow("Blank", blank)

# Draw inside blank page
# blank[:] = 0, 150, 0  # colors all the pixels
# cv.imshow("Colored Page", blank)

# Draw Rectangle
cv.rectangle(blank, (50, 200), (550, 500), (0, 150, 0), thickness=-1)

# Draw a circel
cv.circle(blank, (280, 350), 100, (0,0,255), thickness=-1)
# Draw a line
cv.line(blank, (50, 190), (50, 600), color=(250, 250, 250))
cv.imshow("Bangladeshi Flag", blank)
cv.waitKey(0)
quit()
