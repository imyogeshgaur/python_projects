import cv2

path=r"D:\Users\YOGESH GAUR\PycharmProjects\opencv\download.png"
img = cv2.imread(path)

cv2.imshow('Original Image',img)
cv2.waitKey(0)

imgScale = cv2.resize(img,None,fx=.75,fy=.75)
cv2.imshow('Scaling image',imgScale)
cv2.waitKey(0)

imgScale1 = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow('Scaling image',imgScale1)
cv2.waitKey(0)

imgScale2 = cv2.resize(img,None,(900,400),interpolation=cv2.INTER_AREA)
cv2.imshow('Scaling image',imgScale2)
cv2.waitKey(0)
cv2.destroyAllWindows()