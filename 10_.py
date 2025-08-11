
import cv2
import numpy as np

frame = cv2.imread("D:\\balls.jpg")
frame=cv2.resize(frame, (600,400))

def nothing(x):
    pass
cv2.namedWindow("color Adjustment")


cv2.createTrackbar("lower_h","color Adjustment", 0, 255, nothing)
cv2.createTrackbar("lower_s","color Adjustment", 0, 255, nothing)
cv2.createTrackbar("lower_v","color Adjustment", 0, 255, nothing)

cv2.createTrackbar("upper_h","color Adjustment", 0, 255, nothing)
cv2.createTrackbar("upper_s","color Adjustment", 0, 255, nothing)
cv2.createTrackbar("upper_v","color Adjustment", 0, 255, nothing)


while True:
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h=cv2.getTrackbarPos("lower_h", "color Adjustment")
    l_s=cv2.getTrackbarPos("lower_s", "color Adjustment")
    l_v=cv2.getTrackbarPos("lower_v", "color Adjustment")
    
    u_h=cv2.getTrackbarPos("upper_h", "color Adjustment")
    u_s=cv2.getTrackbarPos("upper_s", "color Adjustment")
    u_v=cv2.getTrackbarPos("upper_v", "color Adjustment")
    
    lower_bound = np.array([l_h,l_s,l_v])
    upper_bound = np.array([u_h,u_s,u_v])
    
    mask = cv2.inRange(hsv,lower_bound,upper_bound)
    
    res = cv2.bitwise_and(frame, frame,mask=mask)
    
    cv2.imshow("original frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res", res)
    
    key=cv2.waitKey(1)
    if key==27:
        break
cv2.destroyAllWindows()    




