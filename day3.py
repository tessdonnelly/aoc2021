import numpy as np

with open("input3.txt", "r") as f:
    lines = f.readlines()


gammaList = []
epsilonList = [] 
i = 0
binaryLength = len(lines[0])-1

while i < binaryLength:
    temp = []
    for line in lines:
        temp.append(line[i])
    temp2 = np.bincount(temp)
    if temp2[0] > temp2[1]: 
        gammaList.append(0)
        epsilonList.append(1)
    if temp2[0] < temp2[1]: 
        gammaList.append(1)
        epsilonList.append(0)
    if temp2[0] == temp2[1]:
        gammaList.append(1)
        epsilonList.append(0)    
    i+=1

gamma = int("".join(str(i) for i in gammaList),2)
epsilon = int("".join(str(i) for i in epsilonList),2)

print (int(gamma*epsilon))

# part 2 

oxy = lines
co2 = lines
    

x = 0
while x < binaryLength:
    tempOxy = []
    temp = []
    for line in oxy:

        # figure out which is the most common
        temp.append(line[x])
    temp2 = np.bincount(temp)

    if temp2[0] > temp2[1]: mostCom = 0
    if temp2[0] < temp2[1]: mostCom = 1
    if temp2[0] == temp2[1]: mostCom = 1
    for line in oxy:
        if int(line[x]) == mostCom:
             tempOxy.append(line)
    
    oxy = tempOxy
    x+=1
    if len(oxy) == 1: break

print ('oxy', oxy)

y = 0
while y < binaryLength:
    tempCo2 = []
    temp = []
    for line in co2:
        # figure out which is the most common
        temp.append(line[y])
    temp2 = np.bincount(temp)

    if temp2[0] > temp2[1]: leastCom = 1
    if temp2[0] < temp2[1]: leastCom = 0
    if temp2[0] == temp2[1]: leastCom = 0
    for line in co2:
        if int(line[y]) == leastCom:
             tempCo2.append(line)
    
    co2 = tempCo2
    y+=1
    if len(co2) == 1: break
            
print ('co2', co2)            

oxyDec = int("".join(str(i) for i in oxy),2)
co2Dec = int("".join(str(i) for i in co2),2)

print (oxyDec)
print (co2Dec)
print (oxyDec*co2Dec)

