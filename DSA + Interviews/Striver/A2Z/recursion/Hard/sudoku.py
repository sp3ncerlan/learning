from collections import defaultdict

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
   
def func(board):
    ROWS, COLS = len(board), len(board[0])
    
    row_set = [set() for _ in range(ROWS)]
    col_set = [set() for _ in range(COLS)]
    grid_set = defaultdict(set)
    ans = []
    
    for row in range(ROWS):
        for col in range(COLS):
            value = board[row][col]
            
            if value != '.':
                row_set[row].add(value)
                col_set[col].add(value)
                grid_set[(row // 3, col // 3)].add(value)
    
    def recurse(row, col):
        if col == COLS:
            row += 1
            col = 0
        
        if row == ROWS:
            ans.append([row[:] for row in board])
            return True
        
        if board[row][col] != '.':
            return recurse(row, col + 1)
        
        for i in range(1, 10):
            num = str(i)
            
            if (num not in row_set[row] and
                num not in col_set[col] and
                num not in grid_set[(row // 3, col // 3)]):
                
                row_set[row].add(num)
                col_set[col].add(num)
                grid_set[(row // 3, col // 3)].add(num)
                board[row][col] = str(num)
                
                if recurse(row, col + 1):
                    return True
                
                board[row][col] = '.'
                row_set[row].remove(num)
                col_set[col].remove(num)
                grid_set[(row // 3, col // 3)].remove(num)
                
        return False

    recurse(0, 0)
    return ans

print(func(board))

"""
Problem Statement: Create a program that fills in the blank cells in a Sudoku puzzle to solve it. Every sudoku solution needs to follow to these guidelines:
1) In every row, the numbers 1 through 9 must appear exactly once.
2) In every column, the numbers 1 through 9 must appear exactly once.
3) In each of the grid's nine 3x3 sub-boxes, the numbers 1 through 9 must appear exactly once.
Empty cells are indicated by the '.' character. .
"""
