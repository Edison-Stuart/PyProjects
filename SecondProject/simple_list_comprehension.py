#!/usr/bin/env python3
temps = [221, 234, 340, 230]

# new_temps = []
# for temp in temps:
#     new_temps.append(temp / 10)   can do this is cleaner way

new_temps = [temp / 10 for temp in temps]

print(new_temps)
