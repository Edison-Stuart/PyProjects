#!/usr/bin/env python3
import cv2

face_cascade=cv2.CascadeClassifier("Faces/haarcascade_frontalface_default.xml")
#takes xml file containing facial recognision data

img=cv2.imread("Faces/photo.jpg")
#reads our image to a variable

grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Changes image to grayscale

faces=face_cascade.detectMultiScale(grey_img,
scaleFactor=1.1,
minNeighbors=5)
#detects where faces are based on xml file data

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)
#draws a green rectangle around faces that are detected

print(type(faces))
print(faces)

resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
#resizes our image and then shows us a window of the new image
cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
