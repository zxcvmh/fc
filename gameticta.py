from tictactoe import HumanPlayer,Computer, GeniusComputer
import time
class tictac:
    def __init__(self):
        self.board= [' ' for _ in range(9)]
        self.current_winner = None
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + "| ".join(row) + "| ") # "| ".join(row) dùng để nối các phần tử trong row
            # 2 "|" là hai đường thẳng biên 

    def print_board_nums(self):
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + "| ".join(row) + "| ")

    def available_moves(self):
        #return []
        moves =[]
        for(i,spot) in enumerate(self.board):
            if(spot == " "):
                moves.append(i)
        return moves
    
    def empty_square(self) -> bool:
        return " " in self.board
    
    def num_empty_square(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if(self.board[square]== " "):
            self.board[square]= letter
            if self.winner(square,letter):
                self.current_winner= letter
            return True
        else: return False

    def winner(self, square, letter):
        #check row
        row_idx= square//3
        row = self.board[row_idx*3: (row_idx+1)*3]
        if all([spot== letter for spot in row]):
            return True
        #check collum
        col_idx= square%3
        col = [self.board[col_idx+i*3] for i in range(3)]
        if all([spot== letter for spot in col]):
            return True
        #check diagonals
        if square%2 != 0: return False
        else:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot== letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot== letter for spot in diagonal2]):
                return True
            
        return False

def play(game, x_player, o_player, print_game= True):
    if print_game:
        game.print_board_nums()
    
    letter = 'x'

    while game.empty_square():
        if letter=='o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square,letter):
            if print_game:
                print(letter + f" make a move to square {square}")
                game.print_board()
                print(" ")
            
            if game.current_winner:
                if print_game:
                    print(letter + " win!")
                return letter
        
        if letter == 'o':
            letter = 'x'
        else: 
            letter = 'o'
        time.sleep(0.7)
    if print_game:
            print("It's a tie")   
    

if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = GeniusComputer('o')
    t= tictac()
    play(t,x_player, o_player, print_game=True)