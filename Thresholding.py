import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('Photos/img2.jfif')

cv.imshow('Cat',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#2 types of thresholding-
#1-simple thresholding
threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple Threshold',thresh)

#creating inverse of above thresholding
threshold,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse',thresh_inv)

#2- Adaptive thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Thresholding',adaptive_thresh)

cv.waitKey(0)