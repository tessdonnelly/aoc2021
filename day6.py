import math
import numpy as np


with open("input6.txt", "r") as f:
    lines = f.readlines()

time = 256
lantern_fish = list(map(int,lines[0].split(',')))

# part 1 solution below 
def one_day(timer, index, fish_list, new_fish_list):
    if timer > 0: new_timer =timer-1
    if timer == 0: 
        new_timer = 6
        new_fish_list.append(8)
    fish_list[index] = new_timer

# part 1 solution if you don't care about how long it takes to run
#i = 0
#while i < time:
#    new_fish = []
#    print 'day ', i
#    j = 0
#    for fish in lantern_fish:
#        one_day(fish, j, lantern_fish,new_fish)
#        j+=1
#    for f in new_fish:
#        lantern_fish.append(f)
#    #print lantern_fish
#    i+=1

print ('number of fish at start =', len(lantern_fish))
fish_by_time = np.zeros((9,time+1))

# set up initial state
for fish in lantern_fish:
    fish_by_time[fish][0]+=1

i=1
while i < time+1:
    # fish at 0 equals fish at 1 from i-1
    fish_by_time[0][i] = fish_by_time[1][i-1]
    # fish at 1 equals fish at 2 from i-1
    fish_by_time[1][i] = fish_by_time[2][i-1]
    # fish at 2 equals fish at 3 from i-1
    fish_by_time[2][i] = fish_by_time[3][i-1]
    # fish at 3 equals fish at 4 from i-1
    fish_by_time[3][i] = fish_by_time[4][i-1]
    # fish at 4 equals fish at 5 from i-1
    fish_by_time[4][i] = fish_by_time[5][i-1]
    # fish at 5 equals fish at 6 from i-1
    fish_by_time[5][i] = fish_by_time[6][i-1]
    # fish at 6 equals (fish at 7 and fish at 0) from i-1 
    fish_by_time[6][i] = fish_by_time[7][i-1] + fish_by_time[0][i-1]
    # fish at 7 equals fish at 8 from i-1
    fish_by_time[7][i] = fish_by_time[8][i-1]
    # fish at 8 equals fish at 0 from i-1
    fish_by_time[8][i] = fish_by_time[0][i-1]
    i+=1


print ('number of fish at day', time, '=', "{:.1f}".format(sum(fish_by_time[:,time])))
