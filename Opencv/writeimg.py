import cv2
path=r"D:\Users\YOGESH GAUR\PycharmProjects\opencv\download1.png"
img = cv2.imread(path)
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.imwrite('output.jpg', img)
cv2.destroyAllWindows()