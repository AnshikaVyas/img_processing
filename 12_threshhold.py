# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:29:32 2024

@author: anshika
"""


import cv2
import numpy as np

frame = cv2.imread("D:\\blackNwhite.jpg",0)
frame=cv2.resize(frame, (600,400))
_,th1=cv2.threshold(frame, 50, 255,cv2.THRESH_BINARY)
cv2.imshow("threshhold 1",th1)

_,th2=cv2.threshold(frame, 50, 255,cv2.THRESH_BINARY_INV)
cv2.imshow("threshhold 2",th2)

_,th3=cv2.threshold(frame, 127, 255,cv2.THRESH_TRUNC)
cv2.imshow("threshhold 3",th3)

_,th4=cv2.threshold(frame, 127, 255,cv2.THRESH_TOZERO)
cv2.imshow("threshhold 4",th4)
_,th5=cv2.threshold(frame, 127, 255,cv2.THRESH_TOZERO_INV)
cv2.imshow("threshhold 5",th5)
cv2.imshow("frame",frame)
cv2.waitKey(0)

cv2.destroyAllWindows()    
