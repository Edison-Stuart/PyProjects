#!/usr/bin/env python3
import cv2, time
from VideoCap.VideoCapData import *

video = VideoController()
count = Increment(0)

while True:
    count.add_to_value()      
    
    gray = Out_Gray(video.GetView()) #changes image to grayscale
    cv2.imshow("Capturing",gray) #presents the frame in a window
    
    break_key = cv2.waitKey(1) #waits 1 millisecond
    if break_key == ord('q'):
        break

video.VideoEnd()
print(count.get_value())
