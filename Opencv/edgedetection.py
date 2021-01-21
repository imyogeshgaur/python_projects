import cv2
def sketch(img):

    imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    imagBlur = cv2.GaussianBlur(imgGrey,(5,5),0)

    imgcCanny = cv2.Canny(imagBlur,10,30)

    ret , mask = cv2.threshold(imgcCanny,30,255,cv2.THRESH_BINARY)

    return mask


cap = cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    cv2.imshow("Our live sketch ", sketch(frame))
    if cv2.waitKey(1) == 1000:
        break

cap.release()
cv2.destroyAllWindows()