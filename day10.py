import math
import numpy as np

with open("input10.txt", "r") as f:
    lines = f.readlines()

def is_open(char):
    if char == '{' or char == '(' or char == '<' or char == '[':
        return True
    else: return False

def is_closed(char):
    if char == '}' or char == ')' or char == '>' or char == ']':
        return True
    else: return False

def find_pair(char):
    if char == '{': return '}'
    elif char == '}': return '{'
    elif char == '(': return ')'
    elif char == ')': return '('
    elif char == '<': return '>'
    elif char == '>': return '<'
    elif char == '[': return ']'
    elif char == ']': return '['

def check_corrupted(l, corrupt_list):
    list = []
    for c in l:
        if is_open(c): 
            list.append(c)
#            print 'adding ', c
        elif is_closed(c): 
            pair = find_pair(c)
#            print 'closed char ', c
#            print list
            if pair == list[-1]:
#                print 'found pair'
                list.pop(-1)
            elif pair != list[-1]:
#                print 'corrupted'
                corrupt_list.append(c)
                break
                



corrupts = []
to_remove = []
for line in lines:
#    print line
    num_corrupt = len(corrupts)
    check_corrupted(line,corrupts)
    if len(corrupts) > num_corrupt:
        to_remove.append(line)

for c_line in to_remove:
    lines.remove(c_line)

paren = corrupts.count(')')
bracket = corrupts.count(']')
curly = corrupts.count('}')
pointy = corrupts.count('>')

syntax_error_score = paren*3 + bracket*57 + curly*1197 + pointy*25137

print ('syntax error score = ', syntax_error_score)

def get_complete(l,complete_list):
    list = []
    for c in l:
        if is_open(c): 
            list.append(c)
        elif is_closed(c): 
            pair = find_pair(c)
            if pair == list[-1]:
                list.pop(-1)
    n_list = []
    for a in list:
        n_list.append(find_pair(a))
    n_list.reverse()
    complete_list.append(n_list)

def get_score(list):
    score = 0
    for l in list:
        value = 0
        if l == ')': value = 1
        elif l == ']': value = 2
        elif l == '}': value = 3
        elif l == '>': value = 4
        score = score*5 + value
    return score

        



completes = []
for incomplete in lines:
    get_complete(incomplete, completes)

scores = []

for comp in completes:
    scores.append(get_score(comp))

middle = int((len(scores)/2))
scores = sorted(scores)

print ('middle score =', scores[middle])



