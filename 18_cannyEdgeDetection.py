import cv2
import numpy as np

img = cv2.imread("D:\\cartoon.jpg")

img = cv2.resize(img,(300,300))
#cv2.imshow("img1", img)
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("img",img2)

#canny = cv2.Canny(img2, 50, 150)
#cv2.imshow("canny", canny)


def nothing(x):
    pass
cv2.namedWindow("canny")
cv2.createTrackbar("Threshhold " ,"canny",0,255,nothing)

while True:
    a = cv2.getTrackbarPos("Threshhold","canny")
    print(a)
    res=cv2.Canny(img2,a,255)
    cv2.imshow("canny",res)
    k=cv2.waiKey(1) & 0XFF
    if k==27:
        break
                 


cv2.destroyAllWindows()  

