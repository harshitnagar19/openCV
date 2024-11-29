import cv2 as cv
import datetime

cap = cv.VideoCapture(0)
while(cap.isOpened()):
    ret , video = cap.read()
    video = cv.putText(video,str(datetime.datetime.now()),(10,50),1,1.0,(0,255,255),1,cv.LINE_AA)
    cv.imshow("video",video)
    k = cv.waitKey(1)
    if(k==ord('s')):
        cv.destroyAllWindows()
        cap.release()
        break
    
