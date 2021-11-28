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

class Increment():
    count_value = 0
    def __init__(self, number):
        self.number = number

    def add_to_value(self):
        Increment.count_value += 1

    def get_value(self):
        return Increment.count_value