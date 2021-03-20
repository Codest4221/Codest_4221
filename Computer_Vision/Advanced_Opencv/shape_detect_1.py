import cv2
import numpy as np
# import image
img = cv2.imread("../fotolar/shapes.png", cv2.IMREAD_GRAYSCALE)
_ , thresh = cv2.threshold(img ,240,255,cv2.THRESH_BINARY)
#find contours
contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


#cv2.drawContours(img,contours,-1,(0,0,0),5)
for contour in contours:

    aprox = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[aprox],0,(0,0,0),4)
    # to count each edge
    aproxtextpoint = np.sum(aprox,axis=0)/len(aprox)
    #print result
    if len(aprox) == 3:
        cv2.putText(img,"Triangle",(int(aproxtextpoint[0][0]),int(aproxtextpoint[0][1])),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
    elif len(aprox)== 4:
        cv2.putText(img, "Rectangle", (int(aproxtextpoint[0][0]), int(aproxtextpoint[0][1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    elif len(aprox) == 5:
        cv2.putText(img, "Pentagon", (int(aproxtextpoint[0][0]), int(aproxtextpoint[0][1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    elif len(aprox) == 6:
        cv2.putText(img, "Hexagon", (int(aproxtextpoint[0][0]), int(aproxtextpoint[0][1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    else:
        cv2.putText(img, "Others", (int(aproxtextpoint[0][0]), int(aproxtextpoint[0][1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.imshow("thresh",thresh)
cv2.imshow("foto", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
