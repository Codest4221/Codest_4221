import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("foto_1.jpg")
imgray = cv2.imread("foto_1.jpg",cv2.IMREAD_GRAYSCALE)
#convert 0-1 value
ret , tresh = cv2.threshold(imgray,150,255,2)
#find contour
countor, hierchy = cv2.findContours(tresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(len(countor))
#draw all
cv2.drawContours(img,countor,-1,(255,255,0),2)
cv2.imshow("foto3",tresh)
cv2.imshow("foto",img)
cv2.imshow("foto1",imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()
