#mouse callback functions
'''
import cv2
import numpy as np

def draw(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(125,0,255),5)
        
    if event ==cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img,(x,y),(x+100,y+75),(125,125,2),2)
        
cv2.namedWindow(winname="res")
img=np.zeros((512,512,3),np.uint8)

cv2.setMouseCallback("res",draw)

while True:
    cv2.imshow("res",img)
    if cv2.waitKey(1) & 0XFF == 27:
        break

cv2.destroyAllWindows()    '''
     
        
import cv2
import numpy as np

def mouse_event(event,x,y,flag,param):
    print("event==",event)
    print("x==",x)
    print("y==",y)
    print("flag==",flag)
    print("parameter==",param)
    font = cv2.FONT_HERSHEY_COMPLEX
    
    if event== cv2.EVENT_LBUTTONDOWN:
        cord = "." + str(x)+","+ str(y)
        cv2.putText(img,cord,(x,y),font,1,(155,124,100),4)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        b=img[y,x,0]
        g=img[y,x,1]
        r=img[y,x,2]
        
        color_bgr = "." + str(b) + "," + str(g) + ","+ str(r)
        cv2.putText(img,color_bgr,(x,y),font,1,(152,255,130),2)
        
cv2.namedWindow(winname="res")

#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread("D:\\output.png")

cv2.setMouseCallback("res", mouse_event)

while True:
    cv2.imshow("res",img)
    if cv2.waitKey(1) & 0XFF == 27:
        break

cv2.destroyAllWindows() 
        
        
    
      
        
           
        