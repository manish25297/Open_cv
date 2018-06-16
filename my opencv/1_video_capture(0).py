from cv2 import *
import numpy as np

a = cv2.VideoCapture(0)                        # a is a variable , cv2.VideoCapture() is a in built function and since we have only one camera on our laptop  which is our primary
                                               #camera so we use "0",# if you have two camera on your system and want to take the picture with the second camera use "1" in place of "0"
                                               # "0"- for primary or first camera         and          "1" = for secondary or second camera 

while True:
    status,img=a.read()                                   #a.read() returns two values:
                                                          #1>.  status = True/False             2>. img=image taken by camera
   # s= cv2.resize(img,(1200,600))
   # cv2.imshow("my_1st_camera_program",s)

    
    cv2.imshow("my_1st_camera_program",img)
                                                          # ord("a")=returns the ascii value of a , ord('q')= returns the ascii value of q
    if cv2.waitKey(100) ==ord('q'):                       # The cv::waitKey(n) function in OpenCV is used to introduce a delay of n milliseconds while rendering images to windows.
         break                                            # When used as cv::waitKey(0) it returns the key pressed by the user on the active window. This is typically used for keyboard
                                                          # input from user in OpenCV programs
 

a.release()
cv2.destroyAllWindows()


"""
-------------------------------------------------------------------------------------------------------------------------------------------------------


The cv::waitKey(n) function in OpenCV is used to introduce a delay of n milliseconds while rendering images to windows. When used as cv::waitKey(0)
it returns the key pressed by the user on the active window. This is typically used for keyboard input from user in OpenCV programs.


char c = cv::waitKey(0);
if ('q' == c)
    QuitProgram();

    
The above function is available in the Python API of OpenCV. However, it seems to return an integer value that cannot be compared to a char like above.
In fact, it is an ASCII value only in the last 8 bits. To use it to compare with a char first mask everything but the first 8 bits and then convert it
using the chr builtin method of Python:

c = cv2.waitKey(0)
if 'q' == chr(c & 255):
    QuitProgram()

--------------------------------------------------------------------------------------------------------------------------------------------------------


SOME EXAMPLES:-



k = cv2.waitKey(33)
    if k==27:    # Esc key to stop
        break
    elif k==-1:  # normally -1 returned,so don't print it
        continue
    else:
        print k # else print its value


        
With this code, I got following values :

Upkey : 2490368
DownKey : 2621440
LeftKey : 2424832
RightKey: 2555904
Space : 32
Delete : 3014656
...... # Continue yourself :)
"""
