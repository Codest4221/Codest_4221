import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("foto.JPG",cv2.IMREAD_GRAYSCALE)
#edge filter method
lap = cv2.Laplacian(img,cv2.CV_64F,ksize= None)
lap = np.uint8(np.absolute(lap))
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1)
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
sobelcombined = cv2.bitwise_or(sobely,sobelx)
sobelcombined = np.uint8(np.absolute(sobelcombined))

cv2.imshow("foto3",sobelcombined)
cv2.imshow("foto",lap)
cv2.imshow("foto1",sobelx)
cv2.imshow("foto2",sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
