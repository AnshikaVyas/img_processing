import cv2
import numpy as np

img = cv2.imread("D:\\distorted2.jpg",0)
img = cv2.resize(img,(300,300))
cv2.imshow("img",img)

kernel = np.ones((5,5),np.float32)/25

#filter
h_filter = cv2.filter2D(img,-1,kernel)
cv2.imshow("homogeneous", h_filter)

blur = cv2.blur(img,(5,5))
cv2.imshow("blur==",blur)

#filter 3 : gaussian filter

gau = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("gau blur ==", gau)

#filter 4 : median filter 
med = cv2.medianBlur(img,5)
cv2.imshow("median filter",med)

#filter : 5 bilateral filter
bi_f = cv2.bilateralFilter(img, 9,75, 75)
cv2.imshow("bi_f",bi_f)

# now plot all the images on graph
titles = ["img","homogeneous","blur","gau blur","median filter","bi_f"]
images=[img,h_filter,blur,gau,med,bi_f]
# if we want to plot it 
from matplotlib import pyplot as plt
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],"grey")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()    







cv2.waitKey(0)

cv2.destroyAllWindows()  

