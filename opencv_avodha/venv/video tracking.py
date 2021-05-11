import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
    _,frame=cap.read()
    cv2.imshow('original',frame)
    new_cap=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('capture',new_cap)

    lower_band=np.array([0, 100, 20])
    upper_band=np.array([10, 255, 255])
    mask=cv2.inRange(new_cap,lower_band,upper_band)
    cv2.imshow('mask',mask)

    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(5) & 0xFF
    if k ==27:
        break
cv2.destroyAllWindows()
