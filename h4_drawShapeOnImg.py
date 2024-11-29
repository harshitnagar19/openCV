import cv2

img = cv2.imread("frog.jpeg",1)

img = cv2.line(img,(0,0),(200,200),(255,255,0),4)
img = cv2.rectangle(img , (20,50),(120,150),(255,0,0),1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,"I'm FROG",(10,150),font,2,(255,0,0),5,cv2.LINE_AA)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()