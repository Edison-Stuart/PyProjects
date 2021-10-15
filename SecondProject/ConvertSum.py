def ListAdd(input):
    output = [float(data) if type(data) == str else data for data in input]
    final_output = sum(output)
    return final_output

print(ListAdd(["1.2", 2.6, "3.3"]))

