import math

def getFuel(fuel):
    next_fuel = math.floor(fuel/3)-2
    
    if next_fuel <= 0:
        print('0', end=' ')
        return 0
    print(next_fuel, end=' ')
    return next_fuel + getFuel(next_fuel)

with open('input.txt', 'r') as file:
    total_fuel = 0
    for line in file:
        mass = int(line)
        print(mass, ': ', end='')
        total_fuel += getFuel(mass)
        print()
    print(total_fuel)