import cv2
import numpy as np
def nothing(x):
    pass

cap = cv2.VideoCapture(0)
#create a window and Bar
cv2.namedWindow("tracking")

cv2.createTrackbar("LH","tracking",0,255,nothing)
cv2.createTrackbar("LS","tracking",0,255,nothing)
cv2.createTrackbar("LV","tracking",0,255,nothing)
cv2.createTrackbar("UH","tracking",255,255,nothing)
cv2.createTrackbar("US","tracking",255,255,nothing)
cv2.createTrackbar("UV","tracking",255,255,nothing)
while 1:
    #frame = cv2.imread("foto.JPG")
    _, frame = cap.read()
    # convert gray scale
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #get bar-value
    l_h = cv2.getTrackbarPos("LH","tracking")
    l_S = cv2.getTrackbarPos("LS", "tracking")
    l_V = cv2.getTrackbarPos("LV", "tracking")
    u_h = cv2.getTrackbarPos("UH", "tracking")
    u_s = cv2.getTrackbarPos("US", "tracking")
    u_v = cv2.getTrackbarPos("UV", "tracking")
    # create Lower-bounded(l_b) and Upper-bounded(u_b)
    l_b = np.array([l_h,l_S,l_V])
    u_b = np.array([u_h,u_s,u_v])
    #Mask and filter 
    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow("mask",mask)
    cv2.imshow("image",frame)
    cv2.imshow("res",res)
    if cv2.waitKey(1)== ord("q"):
        break
cv2.destroyAllWindows()
