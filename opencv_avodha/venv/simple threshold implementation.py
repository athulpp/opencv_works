import cv2
image=cv2.imread('download.png',0)
res,thresh=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow('image',image)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()