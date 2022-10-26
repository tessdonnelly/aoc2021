import numpy as np

class Board():
    def __init__(self, board, index):
        self.board = board
        self.index = index
        self.winning_coords = []
        self.is_winner = False
        self.sum = sum(list(map(sum,self.board)))
    
    def check_winner(self,size_board):
        # check for full column or full row in winnning_coords
        if len(self.winning_coords) > 0:
            x_list = [i[0] for i in self.winning_coords]
            y_list = [i[1] for i in self.winning_coords]
            # check winning row
            most_com_x = max(x_list,key = x_list.count)
            if x_list.count(most_com_x) == size_board:
                self.is_winner = True
                return most_com_x
            # check winning col
            most_com_y = max(y_list,key = y_list.count)
            if y_list.count(most_com_y) == size_board:
                self.is_winner = True
                return most_com_y
        return -1
    
    def has_num(self, num):
        x = 0
        for row in self.board:
            y = 0
            for col in row:
                if col == num:
                    self.add_coord([x,y])
                    self.sum -= num
                y +=1
            x+=1


    def add_coord(self, coord):
        self.winning_coords.append(coord)
        return 

def create_board(board_input, index):
        temp = board_input
        temp_board = []
        for row in temp:
            ints = list(map(int,row.split()))
            temp_board.append(ints)
        b = Board(temp_board,num_boards)
        return b
       

with open("input4.txt", "r") as f:
    lines = f.readlines()


drawing = map(int,lines[0].split(','))
size_board = 5

i = 1
boards = []

# create boards
while i < len(lines):
    num_boards=0
    if lines[i] == '\n':
        num_boards +=1
        b = create_board(lines[i+1:i+6],num_boards)
        i=i+6
        boards.append(b)


#part 1 read drawing, each board has number, each board has winner 
winner = False
for num in drawing:
    if winner != True:
        for b in boards:
            b.has_num(num)
            if b.check_winner(size_board) != -1:
                winner = True
                print ('part 1', b.sum*num)
                break  
"""
# part 2


for num in drawing:
    to_remove = []
    for b in boards:
        b.has_num(num)
        if b.check_winner(size_board) != -1:
            last_winner = b
            to_remove.append(b)
            last_result = last_winner.sum*num
    for c in to_remove:
        boards.remove(c)

print ('part 2, last result ', last_result)
   """     
