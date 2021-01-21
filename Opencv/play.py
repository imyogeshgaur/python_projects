import numpy as np
import cv2 as cv

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(255,255,0),11)
            else:
                cv.circle(img,(x,y),125,(255,0,255),11)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(255,255,0),11)
        else:
            cv.circle(img,(x,y),5,(255,0,255),1)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while True:
    cv.imshow('image',img)
    if cv.waitKey(1)==ord('s'):
        switch=not switch
    if cv.waitKey(1)==27:
        break
cv.destroyAllWindows()