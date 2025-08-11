import cv2
import numpy as np

img = cv2.imread("D:\\girl2.jpg",0)
img = cv2.resize(img,(300,300))
_,mask=cv2.threshold(img,120,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((2,2),np.uint8)


#all morphological operations
e = cv2.erode(mask,kernel)
d = cv2.dilate(mask, kernel)
o = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
c = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
x1 = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
x2 = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
x3 = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)


cv2.imshow("img", img)
cv2.imshow("mask", mask)
cv2.imshow("kernel", kernel)
cv2.imshow("erosion", e)
cv2.imshow("dilation", d)
cv2.imshow("opening", o)
cv2.imshow("closing",c)
cv2.imshow("x1", x1)
cv2.imshow("x2", x2)
cv2.imshow("x3", x3)


cv2.waitKey(0)

cv2.destroyAllWindows()  