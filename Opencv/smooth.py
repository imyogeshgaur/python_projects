import cv2
import numpy as np

path=r"D:\Users\YOGESH GAUR\PycharmProjects\opencv\kec.jfif"
img = cv2.imread(path)
cv2.imshow("Output", img)
cv2.waitKey(0)

#BLUR

# blur1=cv2.blur(img,(3,3))
# cv2.imshow('Blur',blur1)
# cv2.waitKey(0)

#GAUSSIAN BLUR

# blur2=cv2.GaussianBlur(img,(7,7),0)
# cv2.imshow('Gaussian',blur2)
# cv2.waitKey(0)

#MEDIAN BLUR

# blur3=cv2.medianBlur(img,5)
# cv2.imshow('Median',blur3)
# cv2.waitKey(0)

#BILATERAL BLUR

blur4=cv2.bilateralFilter(img,9,75,125)
cv2.imshow('Bilateral',blur4)
cv2.waitKey(0)



