import cv2

path=r"D:\Users\YOGESH GAUR\PycharmProjects\opencv\download3.png"
img = cv2.imread(path)

height,width = img.shape[:2]

startRow,startCol = int(height*.25),int(width*.25)
endRow,endCol = int(height*.90),int(width*.90)

crop = img[startRow:endRow,startCol:endCol]

cv2.imshow('Original Image', img)
cv2.imshow('Cropped Image', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()