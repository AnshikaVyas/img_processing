import cv2
import numpy as np

img1=np.zeros((250,500,3),np.uint8)
img1=cv2.rectangle(img1, (150,150),(210,34), (255,255,255),-1)

img2=np.zeros((250,500,3),np.uint8)
img2=cv2.rectangle(img2,(150,230),(230,34),(255,255,255),-1)

#bitand=cv2.bitwise_and(img1, img2)
#cv2.imshow("bit",bitand)

#bitor=cv2.bitwise_or(img1, img2)
#cv2.imshow("bit",bitor)
#bitnot1=cv2.bitwise_not(img1)
#cv2.imshow("bitnot",bitnot1)

bitxor=cv2.bitwise_xor(img1, img2)
cv2.imshow("bitxor",bitxor)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()



