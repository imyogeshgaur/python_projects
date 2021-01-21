import cv2
import numpy as np

yogi = cv2.VideoCapture(0)

while True:
    ret , frame = yogi.read()
    
    hsv= cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)

    lowerR = np.array([110,50,50])
    upperR = np.array([130,255,255])
  
    
    mask = cv2.inRange(hsv,lowerR,upperR)
    result = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('show',mask)
    cv2.imshow('show 1',result)
    cv2.imshow('show 2',frame)

    if cv2.waitKey()==13:
        break
          
device.release()
cv2.destroyAllWindows()