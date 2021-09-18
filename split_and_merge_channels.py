import cv2 as cv
import numpy as np

img=cv.imread('Photos/img3.jpg')

cv.imshow('Image',img)
#splitting
b,g,r=cv.split(img)
cv.imshow('Blue',b)
cv.imshow('Red',r)
cv.imshow('Green',g)

print(img.shape)
print(b.shape)
print(r.shape)
print(g.shape)

#create a blank image
blank=np.zeros(img.shape[:2],dtype='uint8')

#merging
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('Only Blue',blue)
cv.imshow('Only Red',red)
cv.imshow('Only Green',green)

cv.waitKey(0)

