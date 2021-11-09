#!/usr/bin/env python3

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:  # want to specify which error you are catching
        return("Zero division is meaningless")



print(divide(1,1))
print('End of program')
