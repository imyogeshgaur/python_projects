import cv2
import numpy as np

path=r"D:\Users\YOGESH GAUR\PycharmProjects\opencv\download.png"
img = cv2.imread(path)

#Creating a Kernel Matrix

kernel = np.ones((7,7),np.float32)/49

cv2.imshow('Original Image',img)
cv2.waitKey(0)

blur = cv2.filter2D(img,-1,kernel)
cv2.imshow('7X7 Kernel Blurring ',blur)
cv2.waitKey(0)

kernel