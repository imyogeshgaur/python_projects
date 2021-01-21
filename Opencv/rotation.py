import cv2

path=r"D:\Users\YOGESH GAUR\PycharmProjects\opencv\download1.png"
img = cv2.imread(path)

height,width = img.shape[:2]

rotationMatrix = cv2.getRotationMatrix2D((width/2,height/2),70,.7)

rotatedImg = cv2.warpAffine(img,rotationMatrix,(width,height))

cv2.imshow('Rotated Image', rotatedImg)
cv2.imshow('Original Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()