import cv2
import numpy as np
# to print all mouse-event
event = [i for i in dir(cv2) if "EVENT" in i ]
print(event)
#to setup a function for setMouseCallback-function
def mouseaffect(event,x,y,flags,param ):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y) ,5,(125,125,125),4)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img,(x,y),(x+100,y+100),(200,200,200),3)
    cv2.imshow("image",img)
# read image and edit.
img = cv2.imread("foto.JPG",1)
cv2.imshow("image",img)
cv2.setMouseCallback("image",mouseaffect)

cv2.waitKey(0)
cv2.destroyAllWindows()

