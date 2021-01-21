import cv2
path=r"D:\Users\python\opencv\download.png"
img = cv2.imread(path)
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()