import math
import numpy as np

with open("input9.txt", "r") as f:
    lines = f.readlines()

heightlist = []
for line in lines:
    heightlist.append(list(map(int,list(line.strip()))))

heightmap = np.array(heightlist)

y_max = heightmap.shape[0]
x_max = heightmap.shape[1]


x = 0
y = 0
risk_level_sum = 0
low_points = []

while y < y_max: 
    x = 0
    while x<x_max:
        height = heightmap[y][x]
        up, down, right, left = 10, 10, 10, 10
        if y>0: up = heightmap[y-1][x]
        if y<(y_max-1): down = heightmap[y+1][x]
        if x>0: left = heightmap[y][x-1]
        if x<(x_max-1): right = heightmap[y][x+1]
        if (height < up) and (height < down) and (height < left) and (height < right):
            low_points.append([x, y])
            risk_level = height + 1
            risk_level_sum += risk_level
        x+=1
    y+=1

print ('risk level sum = ', risk_level_sum)

basins=[]

def basin_search(map, point, more_points, checked_points):
    if point in checked_points:
        more_points.remove(point)
    else:
        x = point[0]
        y = point[1]
        if y>0 and (map[y-1][x]!=9): more_points.append([x,y-1])
        if y<(y_max-1) and (map[y+1][x] !=9): more_points.append([x,y+1])
        if x>0 and map[y][x-1] !=9: more_points.append([x-1,y])
        if x<(x_max-1) and map[y][x+1] !=9: more_points.append([x+1,y])
        more_points.remove(point)
        checked_points.append(point)





for point in low_points:
    check_points = []
    check_points.append(point)
    checked_points = []
    while len(check_points)>0:
        for p in check_points:
            basin_search(heightmap,p,check_points,checked_points)

    basins.append(len(checked_points))

print ('basins', sorted(basins))
basins = sorted(basins)
basin_count = len(basins)
print ('3 largest basins multiplied =', basins[basin_count-1]*basins[basin_count-2]*basins[basin_count-3])
