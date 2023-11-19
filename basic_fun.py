import cv2 as cv

img = cv.imread("Photos/cars.jpg")

# Convert to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Cat', img)
cv.imshow('Gary Cars', gray)

# Blur
blur = cv.GaussianBlur(img, (3, 3),cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
canny_blur = cv.Canny(blur, 125, 175)
canny_gray = cv.Canny(gray, 125, 175)
cv.imshow("Canny", canny)
cv.imshow("Blur_Canny", canny_blur) # applying blur will lose more edges
cv.imshow("Gray_canny", canny_gray) # applying blur will lose more edges


# Dilating the image
dilated = cv.dilate(canny_blur, (5,5), iterations=1)
cv.imshow("Dilated", dilated)


resized = cv.resize(blur, (600, 900), interpolation=cv.INTER_LINEAR)
resized_canny = cv.Canny(resized, 120, 170)
cv.imshow("Resized", resized)
cv.imshow("Resized Canny",resized_canny)

# Cropped
cropped = img[100:200, 150:200]
cv.imshow("Cropped",cropped)

cv.waitKey(0)
quit()