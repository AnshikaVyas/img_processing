import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

def nothing(X):
    pass


cv2.namedWindow("color Adjustment",cv2.WINDOW_NORMAL)
cv2.resizeWindow("color Adjustment",(300,300))
cv2.createTrackbar("Thresh","color Adjustment", 0, 255, nothing)

#color detection trackbars
cv2.createTrackbar("Lower_H","color Adjustment", 0, 255, nothing)
cv2.createTrackbar("Lower_S","color Adjustment", 0, 255, nothing)
cv2.createTrackbar("Lower_V","color Adjustment", 0, 255, nothing)
cv2.createTrackbar("Upper_H","color Adjustment", 255, 255, nothing)
cv2.createTrackbar("Upper_S","color Adjustment", 255, 255, nothing)
cv2.createTrackbar("Upper_V","color Adjustment", 255, 255, nothing)

while True:
    _,frame = cap.read()
    frame = cv2.resize(frame,(300,300))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos("Lower_H", "color Adjustment")
    l_s=  cv2.getTrackbarPos("Lower_S", "color Adjustment")
    l_v=  cv2.getTrackbarPos("Lower_V", "color Adjustment")
    
    u_h =  cv2.getTrackbarPos("Upper_H", "color Adjustment")
    u_s =  cv2.getTrackbarPos("Upper_S", "color Adjustment")
    u_v =  cv2.getTrackbarPos("Upper_V", "color Adjustment")
    
    lower_bound = np.array([l_h,l_s,l_v])
    upper_bound = np.array([u_h,u_s,u_v])
    
    #creating mask 
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    #filter mask with image 
    filter = cv2.bitwise_and(frame , frame,mask = mask)
    
    mask1 = cv2.bitwise_not(mask)
    m_g = cv2.getTrackbarPos("Thresh", "color Adjustment")
    
    ret,Thresh = cv2.threshold(mask1,m_g,255,cv2.THRESH_BINARY)
    dilata = cv2.dilate(Thresh,(1,1),iterations=6)
    
    cnts,hier = cv2.findContours(Thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:
        epsilon = 0.0001*cv2.arcLength(c,True)
        data = cv2.approxPolyDP(c, epsilon, True)
        
        hull = cv2.convexHull(data)
        cv2.drawContours(frame, [c],-1,(50,50,150),2)
        cv2.drawContours(frame, [hull],-1, (0,255,0),2)
    
    cv2.imshow("Thresh",Thresh)
    cv2.imshow("mask==",mask)
    cv2.imshow("mask1",mask1)
    cv2.imshow("filter==",filter)
    cv2.imshow("REsult",frame)
   
    key = cv2.waitKey(25) &0xFF
    if key == 27:
       break
   
cap.release()
cv2.destroyAllWindows()    
     
    
    

    