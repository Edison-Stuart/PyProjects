#!/usr/bin/env python3
import cv2
import glob


images=glob.glob("BatchPhotos/*.jpg")
print(images)
# takes a directory of jpg images and makes them into
# a list of file paths

for image in images: # loop over the list and apply changes to images
    print(image)
    img=cv2.imread(image,0) #read in image
    re=cv2.resize(img,(100,100)) 
    cv2.imshow('Hey',re) #display a window
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite(image,re) #save resized image
