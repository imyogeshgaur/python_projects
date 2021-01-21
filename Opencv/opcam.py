import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    hsv= cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)
    
    lowerR = np.array([110,30,30])
    upperR = np.array([130,255,255])

    mask = cv2.inRange(hsv,lowerR,upperR)

    cv2.imshow('show',mask)

   
    if cv2.waitKey(1) == 1000:
        break

cap.release()
cv2.destroyAllWindows()
