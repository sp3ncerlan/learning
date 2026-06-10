from itertools import permutations
import math

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
target = 8

def func(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    
    left, right = 0, ROWS * COLS - 1
    while left <= right:
        mid = (left + right) // 2
        
        value = matrix[mid // COLS][mid % COLS]
        if value == target:
            return True
        elif value > target:
            right = mid - 1
        else:
            left = mid + 1
            
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

"""
