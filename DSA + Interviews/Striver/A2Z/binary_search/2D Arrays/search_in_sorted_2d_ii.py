from itertools import permutations
import math

matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16], [10, 13, 14, 17]]
target = 9

def func(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    
    row, col = 0, COLS - 1
    while row < ROWS and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    
    return False

print(func(matrix))

"""
BF:
- one way is to iterate through all cells, and if we come across target, return True
- o(m * n), o(1)

BETTER:
- we check the first and last element of each row, and if they are <= or >= the target respectively, then we binary search through it
- o(m * logn) where n is the number of columns since we just search one row really

OPTIMAL:
- start from top right corner, everything to the left is less than it, everything below is greater than it
- o(n + m)
"""
