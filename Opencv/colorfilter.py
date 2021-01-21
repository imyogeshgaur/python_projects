import cv2
import numpy as np

device = cv2.VideoCapture(0)

while True:
    ret , frame = device.read()
    
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerR = np.array([110,50,50])
    upperR = np.array([130,255,255])

    mask = cv2.inRange(hsv,lowerR,upperR)

    cv2.imshow('show',mask)
    cv2.imshow('show 1',frame)

    if cv2.waitKey(0)==1000:
        break

device.release()
cv2.destroyAllWindows()
    