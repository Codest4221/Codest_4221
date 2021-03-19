import cv2
import numpy as np

img = cv2.imread("foto.JPG",1)
#img = np.zeros([512,512,3],np.uint0)
cv2.line(img,(0,0),(255,255),(255,100,100),4)
#to create aline
cv2.arrowedLine(img,(255,255),(400,111),(5,10,255),3)
#to cread arrow and line they ara combined
cv2.rectangle(img,(100,50),(150,12),(255,255,255),6)
cv2.rectangle(img,(600,400),(700,200),(0,0,0),-1)
#to create a rectangle
cv2.circle(img,(200,200),200,(255,0,0),2)
#to create a circle
cv2.putText(img,"Merhaba",(100,400),cv2.FONT_HERSHEY_SIMPLEX,4,(100,0,0),4)
# to create a text (foto,yazi,start,font,boyut,renk,incelik)





cv2.imshow("fotos",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
