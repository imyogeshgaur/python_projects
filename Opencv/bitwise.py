import cv2
import numpy as np

#square
 
square=np.zeros((300,300),np.uint8)

cv2.rectangle(square,(50,50),(250,250),134,-1)  
cv2.imshow('Square',square) 
cv2.waitKey(-1)

# half ellipse

ellipse=np.zeros((300,300),np.uint8)

cv2.ellipse(ellipse,(150,150),(150,150),180,0,180,134,-1)  
cv2.imshow('Ellipse',ellipse) 
cv2.waitKey(-1)

#AND OPERATION

andOperation = cv2.bitwise_and(square,ellipse)
cv2.imshow('And Operation',andOperation)
cv2.waitKey(-1)

#OR OPERATION

orOperation = cv2.bitwise_or(square,ellipse)
cv2.imshow('Or Operation',orOperation)
cv2.waitKey(-1)

#XOR OPERATION 

xorOperation = cv2.bitwise_xor(square,ellipse)
cv2.imshow('XOR Operation',xorOperation)
cv2.waitKey(-1)

# NOT OPERATION

notOperation = cv2.bitwise_not(square,ellipse)
cv2.imshow('Not Operation',notOperation)
cv2.waitKey(-1)