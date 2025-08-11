import cv2
import numpy as np

img = cv2.imread("D:\\doremon.jpg",)
img = cv2.resize(img,(300,300))
cv2.imshow("img",img)

pd1 = cv2.pyrDown(img)
cv2.imshow("pd1",pd1)
pd2=cv2.pyrDown(pd1)
cv2.imshow("pd2",pd2)

pu1=cv2.pyrUp(pd2)
cv2.imshow("pu1",pu1)
cv2.waitKey(0)

cv2.destroyAllWindows()  