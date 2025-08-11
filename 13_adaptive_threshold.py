
import cv2
import numpy as np

frame = cv2.imread("D:\\newspap.jpg",0)
frame=cv2.resize(frame, (600,400))

_,th1=cv2.threshold(frame, 127, 255,cv2.THRESH_BINARY)
cv2.imshow("threshhold 1",th1)

th2=cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("th21", th2)

th=cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("th22", th)

cv2.imshow("frame",frame)
cv2.waitKey(0)

cv2.destroyAllWindows()    