import numpy as np

with open("input5.txt", "r") as f:
    lines = f.readlines()

vent_lines=[]
border_x = 0
border_y = 0

# put lines into coordinates and find borders
for line in lines:
    a = line.split('->')
    vent = []
    for b in a:
        c = list(map(int,b.split(',')))
        if c[0] > border_x: border_x = c[0]
        if c[1] > border_y: border_y = c[1]
        vent.append(c)
    vent_lines.append(vent)    

grid = np.zeros((border_x+1, border_y+1))


for l in vent_lines:
    x1,y1 = l[0][0],l[0][1]
    x2,y2 = l[1][0],l[1][1]
    if x1 == x2:
        min_y, max_y = min(y1,y2),max(y1,y2)
        while min_y < (max_y +1):
            grid[x1][min_y]+=1
            min_y+=1
    if y1 == y2:
        min_x, max_x = min(x1,x2), max(x1,x2)
        while min_x < (max_x +1):
            grid[min_x][y1]+=1
            min_x+=1
    if y1 != y2 and x1 != x2:
        min_y, max_y = min(y1,y2),max(y1,y2)
        min_x, max_x = min(x1,x2), max(x1,x2)
        if (x1 > x2 and y1 > y2) or (x1 < x2 and y1 <y2): 
            while min_x < (max_x+1):
                grid[min_x][min_y]+=1
                min_y+=1
                min_x+=1
        if (x1 > x2 and y1 < y2) or (x1 < x2 and y1 > y2):
            while min_x < (max_x+1):
                grid[min_x][max_y]+=1
                max_y-=1
                min_x+=1 




print (grid.transpose())
result = np.where(grid >1)  
print ('crosses', len(result[0]))   
        