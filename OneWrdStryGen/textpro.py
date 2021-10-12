#!/usr/bin/env python3
def sentence(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

output = []
while True:
    user_input = input('Say something: ')
    if user_input == "/end":
        break
    else:
        output.append(sentence(user_input))

print(" ".join(output))
