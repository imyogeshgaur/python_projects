import cv2
path=r"D:\Users\YOGESH GAUR\PycharmProjects\opencv\download1.png"
img = cv2.imread(path)
cv2.imshow("output", img)
cv2.waitKey(0)
#one way
#img1 = cv2.imread(path, 0)
#another way
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("output", grey)
cv2.waitKey(0)
cv2.destroyAllWindows()