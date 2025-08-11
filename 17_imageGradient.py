import cv2
import numpy as np

img = cv2.imread("D:\\cartoon.jpg")

img = cv2.resize(img,(300,300))
#cv2.imshow("img1", img)
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("img",img2)

lap = cv2.Laplacian(img2, cv2.CV_64F)
cv2.imshow("laplacian", lap)

lap2= cv2.Laplacian(img2, cv2.CV_64F)
lap2 = np.uint8(np.absolute(lap2))
cv2.imshow("laplacian2", lap2)

lap3= cv2.Laplacian(img2, cv2.CV_64F,ksize=3)
lap3= np.uint8(np.absolute(lap3))
cv2.imshow("laplacian3", lap3)

#sobel operations
sobelx = cv2.Sobel(img2, cv2.CV_64F, 1, 0,ksize=3)
sobely = cv2.Sobel(img2, cv2.CV_64F, 0, 1,ksize=3)
cv2.imshow("sobelx",sobelx)
cv2.imshow("sobely",sobely)


sobelx2= cv2.Sobel(img2, cv2.CV_64F, 1, 0,ksize=3)
sobely2= cv2.Sobel(img2, cv2.CV_64F, 0, 1,ksize=3)


sobelx2=  np.uint8(np.absolute(sobelx2))
sobely2= np.uint8(np.absolute(sobely2))
cv2.imshow("sobelx2",sobelx2)
cv2.imshow("sobely2",sobely2)


#combing x and y 
sobelcombine = cv2.bitwise_or(sobelx2,sobely2)
cv2.imshow("combine",sobelcombine)


                 


cv2.destroyAllWindows()  

