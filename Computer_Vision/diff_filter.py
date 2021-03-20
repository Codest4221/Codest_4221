import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("foto.JPG")
_,mask = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
#Filter method
oness = np.ones((5,5),np.uint8)
dilation = cv2.dilate(mask,oness,iterations=1)
erosion = cv2.erode(mask,oness,iterations=2)
open2 = cv2.morphologyEx(mask,cv2.MORPH_OPEN,oness)
open1 = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,oness)
open3 = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,oness)
open4 = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,oness)
title = ["image","mask","oness","dilation","erosion","open2","open1","open3","open4"]
image = [img,mask,oness,dilation,erosion,open2,open1,open3,open4]


for i in range(len(title)):
    plt.subplot(1,9,i+1) , plt.imshow(image[i],"gray")
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()
