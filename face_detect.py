#to detect faces in openCV using OpenCV haar cascade
import cv2 as cv
import numpy as np

img=cv.imread('Photos/crowd.jpg')

cv.imshow('Person',img)

#convert to gray scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person',gray)

#import and use haar_face.xml file
haar_cascade=cv.CascadeClassifier('haar_face.xml')
#store faces by identifying in rectangle shape
faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6)
#print number of faces detected
print('Number of faces found=',len(faces_rect))

#print rectangle on detected faces
for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected faces',img)
cv.waitKey(0)