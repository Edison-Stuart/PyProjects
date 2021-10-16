#!/usr/bin/env python3

# write to files with "w" as second variable.
with open("files/vegetables.txt", "w") as myfile:
    myfile.write("Tomato\nCucumber\nOnion\n")
    # for seperate lines you use \n or the break line
    myfile.write("Garlic")

# will make new file if one isn't already there

# function that will accept a string and a filepath
# then retun the number of times the string appeared
# in given file

def ocur(string, filepath):
    with open(filepath, "r") as myfile:
        info = myfile.read()
    return info.count(string)

