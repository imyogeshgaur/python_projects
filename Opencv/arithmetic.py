import cv2
import numpy as np

path=r"D:\Users\YOGESH GAUR\PycharmProjects\opencv\download3.png"
img = cv2.imread(path)

cv2.imshow('Original Image',img)
cv2.waitKey(0)

M = np.ones(img.shape,dtype='uint8')*100

add = cv2.add(img,M)
cv2.imshow('Added Image',add)
cv2.waitKey(0)

sub=cv2.subtract(img,M)
cv2.imshow('Subtracted Image',sub)
cv2.waitKey(0)

mult=cv2.multiply(img,M)
cv2.imshow('Multiplication Image',mult)
cv2.waitKey(0)
cv2.destroyAllWindows()


