import cv2

path=r"D:\Users\YOGESH GAUR\PycharmProjects\opencv\download3.png"
img = cv2.imread(path)

small = cv2.pyrDown(img)
large = cv2.pyrUp(img)

cv2.imshow('Original Image',img)
cv2.imshow('Small Image',small)
cv2.imshow('Large Image',large)

cv2.waitKey(0)
cv2.destroyAllWindows()
