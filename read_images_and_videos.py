import cv2 as cv

#resize image or video, this will work for images,videos and live videos
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#change resolution, this will only work for live video
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

#reading images

#return image in the form of matrix of pixels
img=cv.imread('Photos/img1.jfif')

#displays image in new window, let the name of the window='cat'
cv.imshow('cat',img)

#wait for 0 ms untill keyboard key is pressed
#cv.waitKey(0)

#resizing images
resized_image=rescaleFrame(img)
cv.imshow('Image',resized_image)


#reading videos
capture=cv.VideoCapture('Videos/vid1.mp4')

#video is read fame by frame
while True:
    isTrue,frame=capture.read()
    #resized frame
    resized_frame=rescaleFrame(frame,0.75)
    #show frame by frame
    cv.imshow('Video',frame)
    cv.imshow('Resized Image',resized_frame)

    #if letter d is pressed then exit
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()