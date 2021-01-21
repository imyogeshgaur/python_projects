import cv2
path=r"D:\Users\YOGESH GAUR\PycharmProjects\opencv\download.png"
img = cv2.imread(path,0)
cv2.imshow("output", img)
cv2.waitKey(0)

height,width = img.shape

#SLOPE EDGES
sobX = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobY = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

cv2.imshow("Edge X", sobX)
cv2.waitKey(0)

cv2.imshow("Edge Y", sobY)
cv2.waitKey(0)

#whole edge detection

sob = cv2.bitwise_or(sobX,sobY)
cv2.imshow("Edge detect", sob)
cv2.waitKey(0)

#LAPLACIAN EDGE DETECTION

lap = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("Laplace", lap)
cv2.waitKey(0)

#CANNY EDGE DETECTION

can = cv2.Canny(img,20,170)
cv2.imshow('Canny Edge',can)
cv2.waitKey(0)