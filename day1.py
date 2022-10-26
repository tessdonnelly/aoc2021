with open("input1.txt", "r") as f:
    lines = f.readlines()

inc = 0
dec = 0
equ = 0
i = 1


while i < len(lines):
    prev = int(lines[i-1])
    next = int(lines[i])
    if prev > next: dec+=1
    if next > prev: inc+=1 
    if next == prev: equ+=1
    i+=1

print("part1")
print(inc)

## part 2 

inc3 = 0
dec3 = 0
equ3 = 0 

j = 3

while j < len(lines):
    a1 = int(lines[j-3])
    a2 = int(lines[j-2])
    a3 = int(lines[j-1])
    b1 = int(lines[j-2])
    b2 = int(lines[j-1])
    b3 = int(lines[j])
    asum = a1+a2+a3
    bsum = b1+b2+b3
#    print asum
#    print bsum
    if asum > bsum: dec3+=1
    if asum < bsum: inc3+=1
    if asum == bsum: equ3+=1
    j+=1




print("part2")
print(inc3)
