#!/usr/bin/env python3

# myfile = open("Fruits.txt")
# content = myfile.read()
# myfile.close

with open("files/Fruits.txt") as myfile:
    content = myfile.read()


print(content)