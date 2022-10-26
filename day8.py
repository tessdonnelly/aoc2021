import math
import numpy as np

with open("input8.txt", "r") as f:
    lines = f.readlines()


instances = 0 

for line in lines:
    l = line.split('|')
    output = l[1].strip().split(' ')
    for o in output:
        if len(o) == 2 or len(o) == 3 or len(o) == 4 or len(o) == 7:
            instances+=1


print ('number of instances =', instances)

sum_outputs = 0

for line in lines:
    l = line.split('|')
    output = l[1].strip().split(' ')
    digits = []
    for o in output:
       #print (sorted(o))
        if len(o) == 2:
            digits.append(1)
        if sorted(o) == sorted('gcdfa'):
            digits.append(2)
        if sorted(o) == sorted('fbcad'):
            digits.append(3)
        if sorted(o) == sorted('cdfbe'):
            digits.append(5)
        if len(o) == 4:
            digits.append(4)
        if sorted(o) == sorted('cdfgeb'):
            digits.append(6)
        if sorted(o) == sorted('cefabd'):
            digits.append(9)
        if sorted(o) == sorted('cagedb'):
            digits.append(0)
        if len(o) == 3:
            digits.append(7)
        if len(o) == 7:
            digits.append(8)
    strings = [str(i) for i in digits]
    string = "".join(strings)
    digit = int(string)
   #print ('output = ', output, ' sum = ', digit)
    sum_outputs += digit

print ('total outputs =', sum_outputs)
        
