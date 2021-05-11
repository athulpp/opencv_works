import cv2
import numpy as np
image=cv2.imread('stadium.png',1)
blur=cv2.blur(image,(5,5))
cv2.imshow('image',image)
cv2.imshow('blur',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()