#!/usr/bin/env python3


temps = [221, 234, -9999, 230,]

new_temps = [temp / 10 for temp in temps if temp != -9999]

new_temps2 = [temp / 10 if temp != -9999 else 0 for temp in temps] #using a for loop in conditional


print(new_temps)
print(new_temps2)




