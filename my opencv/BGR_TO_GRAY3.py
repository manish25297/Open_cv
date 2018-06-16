import cv2
import numpy as np

a= cv2.VideoCapture(0)

while(True):
    status,image=a.read()
    g=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("color image",image)
    
    cv2.imshow("gray image",g)

    b=cv2.waitKey(1)
    if b==ord("q"):
        break

a.release()
cv2.destroyAllWindows()
