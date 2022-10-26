with open("input8.txt", "r") as f:
    lines = f.readlines()

def decode(signal, output, digits):
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    zero = []
    for item in signal:
        if len(item) == 2:
            one = item
        if len(item) == 4:
            four = item
        if len(item) == 3:
            seven = item
        if len(item) == 7:
            eight = item
    for s in signal:
        if len(s) == 5:
            if len(set(s) & set(one))==2:
                three = s
            elif len(set(s) & set(four))==3:
                five = s
            elif len(set(s) & set(four))==2:
                two = s
        elif len(s) == 6:
            if len(set(s) & set(four))==4:
                nine = s
            elif len(set(s) & set(one))==2:
                zero = s
            elif len(set(s) & set(one))!=2:
                six = s

    for o in output:
        if sorted(o) == sorted(one): digits.append(1)
        elif sorted(o) == sorted(two): digits.append(2)
        elif sorted(o) == sorted(three): digits.append(3)
        elif sorted(o) == sorted(four): digits.append(4)
        elif sorted(o) == sorted(five): digits.append(5)
        elif sorted(o) == sorted(six): digits.append(6)
        elif sorted(o) == sorted(seven): digits.append(7)
        elif sorted(o) == sorted(eight): digits.append(8)
        elif sorted(o) == sorted(nine): digits.append(9)
        elif sorted(o) == sorted(zero): digits.append(0)

sum_outputs=0

for line in lines:
    l = line.split('|')
    signal = l[0].strip().split(' ')
    output = l[1].strip().split(' ')
    digits = []
    decode(signal, output, digits)

    strings = [str(i) for i in digits]
    string = "".join(strings)
    digit = int(string)
#    print 'output = ', output, ' sum = ', digit
    sum_outputs += digit

print ('total outputs =', sum_outputs)
    