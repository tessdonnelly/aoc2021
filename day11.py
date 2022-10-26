import math
import numpy as np

with open("input11.txt", "r") as f:
    lines = f.readlines()

octopus_list = []
for line in lines:
    octopus_list.append(list(map(int,list(line.strip()))))

octopus_map = np.array(octopus_list)
print ('original map')
print (octopus_map)

step_max = 2000
i = 0
x_max = octopus_map.shape[1]
y_max = octopus_map.shape[0]


def map_flash():
    count = 0
    flash = 10
    while flash in octopus_map:
        y = 0
        while y < y_max:
            x = 0
            while x < x_max:
                if octopus_map[y][x] == 10:
                    inc_flash(x,y)
                    count+=1
                x+=1
            y+=1
    octopus_map[octopus_map > 10] = 0
    return count

def inc_flash(x,y): 
    octopus_map[y][x]+=1
    if y>0 and octopus_map[y-1][x]<10: octopus_map[y-1][x]+=1
    if y<(y_max-1) and octopus_map[y+1][x]<10: octopus_map[y+1][x]+=1
    if x>0 and octopus_map[y][x-1]<10: octopus_map[y][x-1]+=1
    if x<(x_max-1) and octopus_map[y][x+1]<10: octopus_map[y][x+1]+=1
    if y>0 and x>0 and octopus_map[y-1][x-1]<10: octopus_map[y-1][x-1]+=1
    if y>0 and x<(x_max-1) and octopus_map[y-1][x+1]<10: octopus_map[y-1][x+1]+=1
    if y<(y_max-1) and x>0 and octopus_map[y+1][x-1]<10: octopus_map[y+1][x-1]+=1
    if x<(x_max-1) and y<(y_max-1) and octopus_map[y+1][x+1]<10: octopus_map[y+1][x+1]+=1


def increment_all():
    y = 0
    while y < y_max:
        x = 0
        while x < x_max:
            octopus_map[y][x]+=1
            x+=1
        y+=1


flash_total = 0
while i < step_max:
    increment_all()
    flashes = map_flash()
    flash_total += flashes
    if flashes == 100:
        print ('synchronized flashes at step', i+1)
        break
    i+=1

print ('flash total =', flash_total)

