# -*- coding: utf-8 -*-
'''
import cv2
#cap = cv2.VideoCapture("D:\\video.mp4")

#capture video from webcam and save into memry
cap= cv2.VideoCapture(0,cv2.CAP_DSHOW)
#DIVX,XVID , MJPG,X264,WMV1,WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")
#IT CONTAINS FOUR PARAMETERS,name,codec,fps,resolution
output = cv2.VideoWriter("output_grey.avi",fourcc,20.0,(640,480),0)
print("cap",cap)

while cap.isOpened():
    ret,frame = cap.read()
    if ret== True:
        
        #frame = cv2.resize(frame,(700,450))
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",frame)
        cv2.imshow("grey", grey)
        output.write(grey)
        k = cv2.waitKey(100)
        if k ==ord("q") & 0xFF:
            break
cap.release()
output.release()
cv2.destroyAllWindows()'''



# program to connect your laptop to android device
import pafy
import yt_dlp
import cv2



url= "https://www.youtube.com/watch?v=PAuco4ehQUE&t=6018s"
data = pafy.new(url)
data = data.getbest(preftype="mp4")

#capture video from webcam and save into memry
cap= cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(data.url)
print("check==",cap.isOpened())
#DIVX,XVID , MJPG,X264,WMV1,WMV2
#it is 4 byte code which is used to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
#IT CONTAINS FOUR PARAMETERS,name,codec,fps,resolution
output = cv2.VideoWriter("output_android.mp4",fourcc,20.0,(640,480))


while cap.isOpened():
    ret,frame = cap.read()
    if ret== True:
        
        frame = cv2.resize(frame,(700,450))
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",frame)
       # cv2.imshow("grey", grey)
        #output.write(frame)
        k = cv2.waitKey(100)
        if k ==ord("q") & 0xFF:
            break
cap.release()
output.release()
cv2.destroyAllWindows()


