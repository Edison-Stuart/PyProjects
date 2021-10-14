#!/usr/bin/env python3

def area(a , b):
    return a * b

def combine(one, two):
    return one + " " + two


print(area(20, 1050)) # non keyword argument
print(area(b=28, a=1050))  # keyword argument
# note the keyword argument can be passed in any order



