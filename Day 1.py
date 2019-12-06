import math

day_1_input = open("AoC Day 1 Input.txt", "r")
total_mass = 0
for module in day_1_input:
    total_mass = total_mass + (math.floor((int(module) / 3))-2)
    print(module)
    print(total_mass)
day_1_input.close()
