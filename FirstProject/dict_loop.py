#!/usr/bin/env python3

student_grades = {'Marry': 9.1, 'Sim': 8.8, 'John': 7.5}

# for grades in student_grades.items():  #prints out key and value in tuple
#     print(grades)

# for grades in student_grades.keys():  #prints out just the keys in string form
#     print(grades)

# for grades in student_grades.values():
#     print(grades)

# commented out because not efficent use of functions
# def data_printer(data):
#     out = []
#     answer = input("Do you want keys, values, or items?: ")
#     if answer in("keys key Keys Key"):
#         for key in data.keys():
#             out.append(key)
#         return out
#     elif answer in("values value Values Value"):
#         for value in data.values():
#             out.append(value)
#         return out
#     elif answer in("items item Items Item"):
#         print("answer item")
#         for item in data.items():
#             out.append(item)
#         return out
#     else:
#         return "Not an option, please enter key value or item"

def data_printer_item(data):
    out = []
    for item in data.items():
        out.append(item)
    return out

def data_printer_key(data):
    out = []
    for key in data.keys():
        out.append(key)
    return out

def data_printer_value(data):
    out = []
    for value in data.values():
        out.append(value)
    return out



print(data_printer_value(student_grades))

