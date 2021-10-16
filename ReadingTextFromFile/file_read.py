#!/usr/bin/env python3

myfile = open("files/Fruits.txt") # creates a file object 
# print(myfile.read()) file has .read() method
# print(myfile.read()) cursor ends first read at bottom of text

# if you want to print multiple copies of the file
# save it to a variable
content = myfile.read()

myfile.close()
# you should close the file after you are finished processing it

print(content)
