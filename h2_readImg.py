import cv2 as cv 

img = cv.imread("frog.jpeg",1)           # read any image

print(img)
cv.imshow("image",img)                    # show image on window 
keyPressed = cv.waitKey(0)                # hold the window until any key is pressed
# cv.destroyAllWindows() 

# logics
if(keyPressed ==27):
    cv.destroyAllWindows()
elif(keyPressed == ord('s')):            # ord is an iinbuilt function that maps a char with its keyNumber
    cv.imwrite("frog_copy.png",img)    # create new image same as FROG 
    cv.destroyAllWindows()            # used to destory all opend python windows
    

