import cv2 as cv

img=cv.imread('Photos/img1.jfif')

cv.imshow('Cat',img)

# 1- Converting BGR image to gray scale image
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


# 2- Blur image
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# 3- Edge Cascade
canny=cv.Canny(img,125,175)
cv.imshow('Canny Edges',canny)

# 4- Dilating the image
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)

# 5- Eroding the image
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)

# 6- Resize the image
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resized',resized)

# 7- Cropping image
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)
