import cv2
path=r"D:\Users\YOGESH GAUR\PycharmProjects\opencv\download1.png"
img = cv2.imread(path)
cv2.imshow('output', img)
cv2.waitKey(0)
ret, bin = cv2.threshold(img, 235, 255, cv2.THRESH_BINARY)
cv2.imshow('output', bin)
cv2.waitKey(0)
cv2.destroyAllWindows()