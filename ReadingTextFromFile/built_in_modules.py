#!/usr/bin/env python3
import time 

while True:
    with open("files/Fruits.txt") as file:
        print(file.read())
        time.sleep(10)