import cv2

path=r"D:\Users\YOGESH GAUR\PycharmProjects\opencv\download.png"
img = cv2.imread(path)

rotImg=cv2.transpose(img)

cv2.imshow('Original Image',img)
cv2.imshow('Rotated Image',rotImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
