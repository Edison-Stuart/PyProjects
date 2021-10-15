#!/usr/bin/env python3

# write to files with "w" as second variable.
with open("files/vegetables.txt", "w") as myfile:
    myfile.write("Tomato\nCucumber\nOnion\n")
    # for seperate lines you use \n or the break line
    myfile.write("Garlic")

# will make new file if one isn't already there