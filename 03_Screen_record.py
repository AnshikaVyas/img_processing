

#screen recording program
import cv2 as c
import pyautogui as p
import numpy as np



#create resolution
rs = p.size()


#filenam'e in which we want to store recording
fn= input(r"plesase enter any file name and path")
#fix the frame rate
fps = 60.0


fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(fn,fourcc,fps,rs)

#create recording module
c.namedWindow("Live_recording",c.WINDOW_NORMAL)
c.resizeWindow("Live_recording",(600,400))

while True:
    img=p.screenshot()
    f=np.array(img)
    output.write(f)
    c.imshow("Live_recording",f)
    if c.waitKey(1) == ord("q"):
        break
output.release()    
c.destroyAllWindows()    
