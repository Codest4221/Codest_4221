import cv2
import numpy as np
#read image and import
img = cv2.imread((filepath), 1)
#convert gray
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#convert 0-1 value each pixels and find contours
_,imgth = cv2.threshold(imgray,240,255,cv2.THRESH_BINARY)
contours ,_ =cv2.findContours(imgth,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(img,contours,-1,(255,255,0),2)
for i in contours:
  """epsilon = 0.1*cv2.arcLength(cnt,True)
     approx = cv2.approxPolyDP(cnt,epsilon,True)
     some shape can not detected perfectly and you want to ignore failure in image so these function help you to ignore any failure you want to ignore.
     Moreover you can determine degree of ignoring by defining epsilon
     area = cv.contourArea(cnt)
     to find area in contours
  """
    apprrox = cv2.approxPolyDP(i,0.01*cv2.arcLength(i,True),True)
    # draw contours
    cv2.drawContours(img,[apprrox],0,(0,0,0),4)
    x = apprrox.ravel()[0]
    y = apprrox.ravel()[1]
    # detect shape 
    if len(apprrox) == 3:
        cv2.putText(img,"triangle", (x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
    elif len(apprrox) == 4:
        cv2.putText(img, "rectange", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    elif len(apprrox) == 5:
        cv2.putText(img, "fiveabgle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    else: cv2.putText(img, "other", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
cv2.imshow("fotose", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
