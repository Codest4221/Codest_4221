import cv2
# open camera 
yakalayici = cv2.VideoCapture(0)
while yakalayici.isOpened() :
    #to capture frame from camera -- "TFSUT" return True-Flase and "degeler" return image as array
    TFSUT, degerler = yakalayici.read()
    # print Width and height of camera 
    print(yakalayici.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(yakalayici.get(cv2.CAP_PROP_FRAME_HEIGHT))
    #to convert RGB into gray scale
    gri = cv2.cvtColor(degerler, cv2.COLOR_BGR2GRAY)
    # to show frame 
    cv2.imshow("video",gri)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
yakalayici.release()
cv2.destroyAllWindows()
