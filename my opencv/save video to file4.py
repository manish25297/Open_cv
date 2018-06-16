import cv2
import numpy as np

a=cv2.VideoCapture(0)                                 # we are taking the image from the primary camera ie. 0
c=cv2.VideoWriter_fourcc(*'XVID')                     #defining the codec 
out=cv2.VideoWriter('output.avi',c,20.0,(640,480))    # output.avi is the name and its extension type , fps= 20.0  i.e if you decrease it to 2.0 you will get a slow motion
                                                      # an  if you increase is you will get a fast action video while we are working on the same speed
while True:
    status,image=a.read()                                 #a.read() returns two values first is true/false and second is the image
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)           #cv2.cvtColor( image, "desired color = here the color is cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("color image",image)                       # color image = title of the window and image = what is going to be shown on that window
    cv2.imshow("gray",gray)                                # we can flip the image using image=cv2.flip(image,1) now you get a mirror img not a default camera image
    out.write(image)                                       # now writing the file 
    

    k=cv2.waitKey(1)              # cv2.waitKey(1) is for delay in image display (in milliseconds) here, it is 1 millisecond note- never put 0 ,otherwise you will get a static image
    if k==ord('q'):               # cv2.waitKey() also returns the 8bit ascii value of the character which is pressed onto the window and ord() is also for getting the ascii value of char
        break
a.release()
out.release()
cv2.destroyAllWindows()
