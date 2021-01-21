import numpy as np
import cv2

draw=False
switch=True
ax,ay = -1,-1

def drawPaint(event,flags,x,y,param):
    global draw,switch,ax,ay 
    
    if event == cv2.EVENT_LBUTTONDOWN:
        draw=True
        ax,ay=x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw ==True:
           if switch==True:
            cv2.rectangle(img,(ax,ay),(x,y),(0,255,255),1)
           else:
            cv2.circle(img,(x,y),25,(123,213,255),1)
    elif event==cv2.EVENT_LBUTTONUP:
        if draw==False:
           if switch==True:
            cv2.rectangle(img,(ax,ay),(x,y),(0,255,255),1)
           else:
            cv2.circle(img,(x,y),25,(123,213,255),1)

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('Image')
cv2.setMouseCallback('Image',drawPaint)
while True:
    cv2.imshow('Image',img)
  
cv2.destroyAllWindows()

