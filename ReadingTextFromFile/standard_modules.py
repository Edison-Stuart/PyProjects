#!/usr/bin/env python3
import time
import os

while True:
    if os.path.exists("files/Fruits.txt"):    
        with open("files/Fruits.txt") as file:
            print(file.read())
    else:
        print("File does not exist")
    time.sleep(10)