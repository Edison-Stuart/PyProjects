#!/usr/bin/env python3
def weather_condition(temperature):
    if temperature > 7:
        return "warm"
    else:
        return "cold"

# user_input = input("Enter temperature:")   user input will be converted into a string, so function won't work

# print(user_input.lower())    can make changes to the user input with methods

user_input = float(input('Enter temperature:')) # We convert the string into a float so our function works
print(weather_condition(user_input))
