with open("input2.txt", "r") as f:
    lines = f.readlines()

depth = 0
horiz = 0
aim = 0

for line in lines:
    command = line.split()
    num = int(command[1])
    if command[0] == 'forward':
        horiz+=num
        depth+=(aim*num)
    if command[0] == 'down':
        aim+=num     
    if command[0] == 'up':
        aim-=num

print (depth)
print (horiz) 
print (aim)       
print (depth*horiz)