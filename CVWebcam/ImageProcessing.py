#!/usr/bin/env python3
import cv2

img=cv2.imread("Photos/galaxy.jpg",0) # reading in the image

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image=cv2.resize(img,(int(img.shape[1]/2),
    int(img.shape[0]/2))) # making the image half its size so it fits in screen
cv2.imshow("Galaxy",resized_image) 
cv2.imwrite("Photos/Galaxy_resized.jpg",resized_image) # resaving new image
cv2.waitKey(0) # waits for user input
cv2.destroyAllWindows()
