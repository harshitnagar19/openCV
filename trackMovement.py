import cv2

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("vtest.avi")


while(cap.isOpened()):
    _,frameOne = cap.read()
    _,frameTwo = cap.read()
    diff = cv2.absdiff(frameOne,frameTwo)
    grey = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY) #convert to grey bcz finding conture in grey is more efficient than BGR
    blur = cv2.GaussianBlur(grey,(5,5),0)
    _,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frameOne,contours,-1,(0,255,0),2)
    # for contour in contours:
    #     (x,y,w,h) = cv2.boundingRect(contour)
    #     if(cv2.contourArea(contour)<700):
    #         continue
    #     cv2.rectangle(frameOne,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("video",frameOne)
    
    if(cv2.waitKey(1)==ord('q')):
        break

cv2.destroyAllWindows()
cap.release()