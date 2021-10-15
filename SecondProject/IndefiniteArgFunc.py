#!/usr/bin/env python3

def mean(*args):
    return sum(args) / len(args)

print(mean(1, 3, 4)) # has to be non keyword argument

def mean2(**kwargs):
    return kwargs  # will allow you to pass keyword arguments

print(mean2(a=1, b=4, c=8))