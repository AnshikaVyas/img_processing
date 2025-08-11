# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 22:12:13 2024

@author: anshika
"""

#result Blending with Trackbars 

import numpy as np
import cv2 as cv
#read two different images of same channel
img1 =cv.imread("D:\\pikachu.jpg")
img1 = cv.resize(img1,(500,700))
img2 =cv.imread("D:\\doremon.jpg")
img2 = cv.resize(img2,(500,700))
    
def blend(x):
    pass

img = np.zeros((400,400,3),np.uint8)
cv.namedWindow('win') #create track bar windows
cv.createTrackbar('alpha','win',1,100,blend)
switch = '0 : OFF \n 1 : ON'  #create switch for invoke the trackbars
cv.createTrackbar(switch,'win',0,1,blend)  #create track bar for switch
while(1):
    alpha = cv.getTrackbarPos('alpha','win')
   
    s = cv.getTrackbarPos(switch,'win')
    na = float(alpha/100)
    
    if s == 0:
        dst = img[:]
    else:
        dst = cv.addWeighted(img1,1-na,img2,na,0)
        cv.putText(dst, str(alpha), (20, 50), cv.FONT_ITALIC,
                   2, (0, 125, 255), 2)
    cv.imshow('dst',dst)

    k=cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
cv.waitKey(0)    

cv.destroyAllWindows()


'''
import cv2
import numpy as np

img1=cv2.imread("D:\\pikachu.jpg")
img1= cv2.resize(img1,(800,800))
img2=cv2.imread("D:\\output.png")
img2= cv2.resize(img2,(800,800))
#to make boorder
#brdr = cv2.copyMakeBorder(img, 10, 10, 5, 5, cv2.BORDER_CONSTANT,value=[255,0,125])
cv2.imshow("img",img1)
cv2.imshow("img",img2)
cv2.imshow("img2",img1)

#blending two images
result2=cv2.add(img1,img2)
cv2.imshow("result2==",result2)


#extended version of add
result1= cv2.addWeighted(img1, 0.3, img2, 0.7,0)
cv2.imshow("result==",result1)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

