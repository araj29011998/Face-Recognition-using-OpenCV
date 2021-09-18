import cv2 as cv
import numpy as np

img=cv.imread('Photos/img1.jfif')

cv.imshow('Cat',img)

#converting to gray scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#finding contours using canny edge detector
canny=cv.Canny(img,125,175)
cv.imshow('Canny Edges',canny)

#thresholding image method for finding contours
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)


contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

#creating blank image
blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)

#drawing contours found on blank image
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn',blank)

cv.waitKey(0)