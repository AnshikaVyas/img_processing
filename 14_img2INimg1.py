
import cv2
import numpy as np

frame1 = cv2.imread("D:\\pikachu.jpg")
frame2 = cv2.imread("D:\\cartoon.jpg")

frame1=cv2.resize(frame1, (1024,650))
frame2=cv2.resize(frame2, (600,650))

# i want to fix image 2 data into img1
r,c,ch=frame2.shape
print(r,c,ch)

#roi
roi = frame1[0:r,0:c]

#now creatring mask for img2
img_gray=cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

#create mask using threshold
_,mask=cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

mask_inv=cv2.bitwise_not(mask)


img1_bg = cv2.bitwise_and(roi, roi,mask=mask_inv)


# take only region of figure from original image
img2_fg=cv2.bitwise_and(frame2, frame2,mask=mask)

res = cv2.add(img1_bg,img2_fg)
cv2.imshow("reslt",res)

#final output
final=frame1
final[0:r,0:c]=res
cv2.imshow("final",final)

#cv2.imshow("frame1", frame1)
#cv2.imshow("frame2",frame2)
#cv2.imshow("frame3",roi)
#cv2.imshow("step1", img_gray)
#cv2.imshow("step2",mask)
cv2.imshow("step3", mask_inv)
cv2.imshow("step4",img1_bg)
cv2.imshow("step5", img2_fg)

cv2.waitKey(0)

cv2.destroyAllWindows()  