import cv2
image=cv2.imread('rono.jpg',1)
cv2.line(image,(0,0),(400,400),(255,0,0),5)
cv2.rectangle(image,(0,0),(100,100),(0,255,0),3)
cv2.circle(image,(100,100),50,(0,0,255),-1)
cv2.putText(image,"hello",(100,100),font,4,(255,255,255),cv2.LINE_AA)
cv2.imshow("shapes",image)
cv2.waitKey(0)
cv2.destroyAllWindows()