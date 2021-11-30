#!/usr/bin/env python3
import cv2, pandas
from datetime import datetime
from VideoCap.VideoCapData import *

first_frame = None
status_list = [None,None]
times = []
df = pandas.DataFrame(columns=["Start","End"])

video = VideoController()
count = Increment(0)

while True:
    count.add_to_value()      
    frame = video.GetView()

    status = 0

    gray = Out_Gray(frame) #changes image to grayscale
    gray = Out_Blur(gray)
    # gray = cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = Frame_Dif(first_frame, gray)
    # delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = Out_Thresh(delta_frame)
    thresh_frame = Out_Dilated(thresh_frame)

    (cnts,_) = Out_Cont(thresh_frame)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status = 1

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)
    status_list.append(status)
    
    
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())


    cv2.imshow("Gray Frame",gray) #presents the frame in a window
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame",frame)

    break_key = cv2.waitKey(1) #waits 1 millisecond
    
    if break_key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)
print(times)
    
for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("Times.csv")

video.VideoEnd()
print(count.get_value())