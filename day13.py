import numpy as np

with open("input13.txt", "r") as f:
    lines = f.read().splitlines()

dots = []
instructions = []
max_x = 0
max_y = 0
for line in lines:
    if line != '' and line[0] is not 'f':
        dot = list(map(int,line.split(',')))
        if dot[0] > max_x: max_x = dot[0]
        if dot[1] > max_y: max_y = dot[1]
        dots.append(dot)
    if line != '' and line[0] is 'f':
        instructions.append(line)
    

def fold_paper_y(fold_index, dot_list, max_x, max_y):
    paper_fold = np.zeros((fold_index+1,max_x+1))
    to_remove = []
    to_add = []
    for d in dot_list:
        x, y = d[0], d[1]
        if y<fold_index:
            paper_fold[y][x]+=1
        elif y  > fold_index:
            y2 = (max_y)-y
            paper_fold[y2][x]+=1
            to_remove.append([x,y])
            to_add.append([x,y2])
        else: to_remove.append([x,y])
    for r in to_remove: dot_list.remove(r)
    for a in to_add: dot_list.append(a)
    return paper_fold

def fold_paper_x(fold_index, dot_list, max_x, max_y):
    to_remove = []
    to_add = []
    paper_fold = np.zeros((max_y+1,fold_index+1))
    for d in dot_list:
        x, y = d[0], d[1]
        if x<fold_index:
            paper_fold[y][x]+=1
        elif x > fold_index:
            x2 = (max_x)-x
            paper_fold[y][x2]+=1
            to_remove.append([x,y])
            to_add.append([x2,y])
        else: to_remove.append([x,y])
    for r in to_remove: dot_list.remove(r)
    for a in to_add: dot_list.append(a)
    return paper_fold


folded_paper = []

i = 0
while i < len(instructions):
    #print 'at step', i, 'max x =', max_x, 'max y =', max_y
    if instructions[i][11] == 'y':
        y_fold = int(instructions[i].split('=')[1].strip())
        folded_paper = fold_paper_y(y_fold,dots,max_x,max_y)
        max_y = y_fold-1
    elif instructions[i][11] == 'x':
        x_fold = int(instructions[i].split('=')[1].strip())
        folded_paper = fold_paper_x(x_fold,dots,max_x,max_y)
        max_x = x_fold-1
    i+=1

print (folded_paper)


    


    