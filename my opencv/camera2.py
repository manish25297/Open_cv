from cv2 import *
import numpy as np

a=cv2.VideoCapture(0)

while(True):
    status,img= a.read()
    cv2.imshow("camera",img)

    k=cv2.waitKey(1)
    if k==ord("q"):
        break
a.release()
cv2.destroyAllWindows()
