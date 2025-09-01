import random
import re 

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size= dim_size
        self.num_bombs= num_bombs
        self.board = self.make_board()
        self.assign_value_to_board()
        self.dug = set()

    def make_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        
        planted= 0

        while planted < self.num_bombs:
            loc  = random.randint(0, self.dim_size**2 -1)
            row=  loc// self.dim_size
            col= loc% self.dim_size

            if board[row][col] == "*":
                continue
            board[row][col] = "*"
            planted +=1

        return board
    
    def assign_value_to_board(self):

        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c]= self.neighboring_bombs(r,c)
        

    def neighboring_bombs(self,row,col):
        num_nb= 0
        
        for r in range(max(0,row-1),min(self.dim_size-1, row+1)+1):
            for c in range(max(0,col-1), min(self.dim_size-1, col+1)+1):
                if row == c and col == c:
                    continue

                if self.board[r][c]== '*':
                    num_nb += 1


        return num_nb
    
    def dig(self, row, col):
        self.dug.add((row,col))
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        for r in range(max(0,row-1),min(self.dim_size-1, row+1)+1):
            for c in range(max(0,col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue # don't dig where you've already dug
                self.dig(r, c)
        return True

    def __str__(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

def play(dim_size=10, num_bombs=10):
    frame = Board(dim_size, num_bombs)
    safe = True

    while len(frame.dug) < frame.dim_size** 2 - num_bombs:
        print(frame)

        r = int(input("choose a row: "))
        c = int(input("choose a collum: "))

        safe = frame.dig(r,c)

        if not safe:
            break 

        if safe:
            print("Congratulation!")
        else:
            print("Sorry game over")
            frame.dug = [(r,c) for r in range(frame.dim_size) for c in range(frame.dim_size)]
            print(frame)

if __name__ == '__main__':
    play()