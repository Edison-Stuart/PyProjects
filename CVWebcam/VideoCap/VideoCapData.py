#!/usr/bin/env python3
import cv2


class VideoController():
    camera_output = cv2.VideoCapture(0)
    def GetView(self):
        check, frame = VideoController.camera_output.read()
        return frame

    def VideoEnd(self):
        VideoController.camera_output.release() #release camera at the end
        cv2.destroyAllWindows

def Out_Gray(photo):
    picture = cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)
    return picture

def Out_Blur(photo):
    blurred_photo = cv2.GaussianBlur(photo,(21,21),0)
    return blurred_photo

def Frame_Dif(control, subject):
    combined_frame = cv2.absdiff(control,subject)
    return combined_frame

def Out_Thresh(photo):
    black_n_white = cv2.threshold(photo, 30, 255,cv2.THRESH_BINARY)[1]
    return black_n_white

def Out_Cont(photo):
    (contours,_) = cv2.findContours(photo.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    return (contours,_)

def Out_Dilated(photo):
    out_photo = cv2.dilate(photo, None, iterations=2)
    return out_photo

class Increment():
    count_value = 0
    def __init__(self, number):
        self.number = number

    def add_to_value(self):
        Increment.count_value += 1

    def get_value(self):
        return Increment.count_value