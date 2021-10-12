#!/usr/bin/env python3
name = input('Enter your name: ')
surname = input('Enter your surname: ')
when = "today"

message = "Hello %s %s!" % (name, surname)
message = f'Hello {name} {surname}. what\'s up {when}' # only works in python 3.6 +
print(message)
