import cv2
import numpy as np

path=r"D:\Users\YOGESH GAUR\PycharmProjects\opencv\download1.png"
img = cv2.imread(path)

height,width = img.shape[:2]
print(height)
print(width)

quaterHeight,quaterWidth = height/4,width/4
print(quaterHeight)
print(quaterWidth)

T = np.float32([[1,0,quaterWidth],[0,1,quaterWidth]])

imgTranslation = cv2.warpAffine(img,T,(width,height))

cv2.imshow('Original Image',img)
cv2.imshow('Translation',imgTranslation)

cv2.waitKey(0)
cv2.destroyAllWindows()