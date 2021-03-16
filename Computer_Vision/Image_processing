
#fotoğrafı girdi yapar
#to import(read) the image
import cv2
foto = cv2.imread("foto.JPG",1)
#Array şeklinde basar 
#print a image as array
print(foto)
#Fotoyu gösterir
#display the image
cv2.imshow("fotoshowing", foto)
#basılan tuşu k ya atar
#Assign an input-letter to "K" 
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord("s") or k == ord("S"):#tuş atama yapar 
    #bu satır fotoyu kaydeder
    #to save photo
    cv2.imwrite("fotocopy.jpg", foto)
    
    cv2.destroyAllWindows()
