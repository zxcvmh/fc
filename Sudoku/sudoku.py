    
def find_next_empty(puzzle):
    for r in range(9):
        for c  in range(9):
            if puzzle[r][c] == -1:
                return r,c
    
    return None,None

def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    col_vals =  [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    row_start =  (row //3)*3
    col_start = (col // 3)*3

    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3):
            if puzzle[i][j] == guess:
                return False
            
    return True



def solve_sudoku(puzzle):

    #step1: choose where is empty 
    row, col = find_next_empty(puzzle)     
    
    #step1.1: if there's nowhere left, then we're done 
    if row is None:
        return True

    #step 2: if there is a place to put a number, then make a guess between 1 and 9 
    for guess in range(1,10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
        
            if solve_sudoku(puzzle):
                return True
            
        puzzle[row][col] = -1

    
