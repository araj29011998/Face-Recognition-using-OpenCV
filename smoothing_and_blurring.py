import cv2 as cv
import numpy as np

img=cv.imread('Photos/img1.jfif')

cv.imshow('Image',img)

# different methods of blurring-
# method 1- Averaging
average=cv.blur(img,(3,3))
cv.imshow('Average Blur',average)

# method 2- Gaussian Blur
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur',gauss)

# method 3- Median Blur
median=cv.medianBlur(img,3)
cv.imshow('Median Blur',median)

# method 4- Bilateral Blur
bilateral=cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral Blur',bilateral)

cv.waitKey(0)