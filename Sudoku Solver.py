# Sudoku test puzzle
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_board(board):
    # Print the Sudoku puzzle
    for row in board:
        print(row)
        
def find_empty_cell(board):
    # Find an empty cell in the Sudoku puzzle
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                return (r, c)  # row, column
    return None

def is_valid(board, num, row, col):
    # Check if the number is not in the current row
    if num in board[row]:
        print("False")
        return False
    # Check if the number is not in the current column
    for i in range(len(board)):
        if board[i][col] == num:
            print("False")
            return False
    # Calculate the starting indices of the 3x3 box
    box_row = (row // 3)*3
    box_col = (col // 3)*3
    # Check if the number is not in the current 3x3 box
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if board[r][c] == num:
                print("False")
                return False
    print("True")
    return True

def solve_sudoku(board):
    empty_cell=find_empty_cell(board)
    if not empty_cell:
        return True  # Puzzle solved
    
    row, col = empty_cell # Get row and column of the empty cell

    for num in range(1, 10): # Try numbers 1-9
        if is_valid(board, num, row, col):
            board[row][col] = num # Place the number in the cell
            if solve_sudoku(board):
                return True # Continue to solve the rest of the puzzle
            board[row][col] = 0 # Reset the cell (backtrack)

    return False # Trigger backtracking

print("Puzzle:")
print_board(board)
solve_sudoku(board)
print("\nSolved Puzzle:")
print_board(board)