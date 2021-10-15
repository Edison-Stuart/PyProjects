#!/usr/bin/env python3

with open("files/vegetables.txt", "a") as myfile:
    myfile.write("\nOkra") # use "a" to append to file
    myfile.seek(0) # this will reset the cursor

