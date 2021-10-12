#!/usr/bin/env python3
from datetime import date #not part of video practice, messing around with python libraries

name = input('Enter your name: ')
surname = input('Enter your surname: ')

when = date.today()
print(type(when))

message = "Hello %s %s!" % (name, surname)
message = f'Hello {name} {surname}. what\'s up {when}' # only works in python 3.6 +
print(message)
