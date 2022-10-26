import math
import numpy as np

with open("input7.txt", "r") as f:
    lines = f.readlines()

crab_positions= list(map(int,lines[0].split(',')))
#print (crab_positions)

i = min(crab_positions)
min_fuel = 1000000000000000000000

while i <= max(crab_positions):
    temp_fuel = 0
    for c in crab_positions:
        moves = abs(c-i)
        temp_fuel += (moves*(moves+1))/2
    if temp_fuel < min_fuel: min_fuel = temp_fuel
   #print ('position', i, 'fuel used = ', temp_fuel)
    i+=1

print (min_fuel)