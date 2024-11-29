import cv2 

cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'avc1')
# out = cv2.VideoWriter("cameraVideo.mp4",fourcc,20.0,(640,480))
while(cap.isOpened()):
    tf , vid = cap.read()
    # out.write(vid)
    cv2.imshow("camera",vid)
    k = cv2.waitKey(1)
    if(k==ord('q')):
        break

cap.release()
out.release()
cv2.destroyAllWindows()