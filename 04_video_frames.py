# break video into multiple images and store in a folder
import cv2

vidcap = cv2.VideoCapture("D:\\hello.mp4")
ret,image = vidcap.read()
count=0
while True:
    if ret == True:
        cv2.imwrite("D:\\frames\\imgN%d.jpg"%count,image)
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        ret,image=vidcap.read()
        
        cv2.imshow("res",image)
        
        count +=1
        if cv2.waitKey() &  0xFF == ord("q"):
            break
        cv2.destroyAllWindows()
        
vidcap.release()
cv2.destroyAllWindows()        



"""
import cv2
import os

# Define video file path and frames directory
video_path = "D:\\hello.mp4"
frames_dir = "D:\\frames"

# Create the frames directory if it doesn't exist
if not os.path.exists(frames_dir):
    os.makedirs(frames_dir)

# Open the video file
vidcap = cv2.VideoCapture(video_path)
ret, image = vidcap.read()
count = 0

while ret:
    # Save the current frame as an image
    cv2.imwrite(os.path.join(frames_dir, "imgN%d.jpg" % count), image)

    # Display the frame
    cv2.imshow("Frame", image)

    # Move forward by a specific time interval (e.g., 1 second)
    vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))
    
    # Read the next frame
    ret, image = vidcap.read()
    
    # Increment the frame counter
    count += 1
    
    # Wait for a short period or break if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
vidcap.release()
cv2.destroyAllWindows()
"""