n = 4
    
def solve(col, board, result, n, row_check, pos_diag, neg_diag):
    if col == n:
        temp = [''.join(row) for row in board]
        result.append(temp)
        return
    
    for row in range(n):
        if (row_check[row] == 0 and
            pos_diag[row + col] == 0 and
            neg_diag[(n - 1) + (col - row)] == 0):
            
            board[row][col] = 'Q'
            row_check[row] = 1
            pos_diag[row + col] = 1
            neg_diag[(n - 1) + (col - row)] = 1
            
            solve(col + 1, board, result, n, row_check, pos_diag, neg_diag)
            
            board[row][col] = '.'
            row_check[row] = 0
            pos_diag[row + col] = 0
            neg_diag[(n - 1) + (col - row)] = 0
   
def func(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    result = []
    
    row_check = [0] * n
    pos_diag = [0] * (2 * n - 1)
    neg_diag = [0] * (2 * n - 1)
    
    solve(0, board, result, n, row_check, pos_diag, neg_diag)
    
    return result

print(func(n))

"""
Problem Statement: The n-queens is the problem of placing n queens on n x n chessboard such that no two queens can attack each other. Given an integer n, return all distinct solutions to the n -queens puzzle. Each solution contains a distinct boards configuration of the queen's placement, where 'Q' and '.' indicate queen and empty space respectively.

Input: N = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown below

Input : N = 1
Output: [["Q"]]
Explanation : There is only one way to place 1 queen on 1x1 chessboard.
"""
