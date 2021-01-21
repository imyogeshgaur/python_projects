import cv2
import numpy as np

yogesh=np.zeros((300,300,4),np.uint8)
cv2.ellipse(yogesh,(150,150),(150,150),180,0,180,(255,200,255),-1)
cv2.imshow('YOYO',yogesh)
cv2.waitKey(0)

mukesh=np.zeros((512,512,4),np.uint8)
cv2.rectangle(mukesh,(100,100),(400,400),(0,255,0),-1)
cv2.imshow('psit',mukesh)
cv2.waitKey(0)

first=np.zeros((512,512,4),np.uint8)
cv2.line(first,(0,0),(511,511),(0,0,255),5)
cv2.imshow('efb',first)
cv2.waitKey(0)

h=np.zeros((512,512,4),np.uint8)
cv2.circle(h,(256,256),256,(255,255,0),-1)
cv2.imshow('YOYO',h)
cv2.waitKey(0)
