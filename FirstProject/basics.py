#!/usr/bin/env python3
# monday_temperatures = [9.1, 8.8, 7.5] List
monday_temperatures = (9.1, 8.8, 7.5) #tuple
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum / length
print(mean)
