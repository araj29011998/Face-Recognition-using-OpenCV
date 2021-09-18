import cv2 as cv
import numpy as np

img=cv.imread('Photos/img1.jfif')

cv.imshow('Cat',img)

# translation function
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# cases possible with values of x and y
# -x --> left
# -y--> up
# x--> right
# y--> down

translated=translate(img,-100,100)
cv.imshow('Translated',translated)

# rotation function
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    # case 1-
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,45)
cv.imshow('Rotated',rotated)

Clockwise_rotated=rotate(img,-90)
cv.imshow('Rotated',Clockwise_rotated)

#resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#flipping with flip code=0 (Flip vertically)
flip=cv.flip(img,0)
cv.imshow('Flip',flip)

cv.waitKey(0)