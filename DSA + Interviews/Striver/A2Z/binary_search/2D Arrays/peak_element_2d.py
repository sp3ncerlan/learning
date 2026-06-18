from itertools import permutations
import math

matrix = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]

def find_max(arr, row):
    n = len(arr)
    max_value = float('-inf')
    index = -1
    
    for i in range(n):
        if arr[i] > max_value:
            max_value = arr[i]
            index = i
    
    return index

def func(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    
    left, right = 0, ROWS - 1
    
    while left <= right:
        row = (left + right) // 2
        max_col = find_max(matrix[row], row)
        value = matrix[row][max_col]
        
        top = matrix[row - 1][max_col] if row - 1 >= 0 else float('-inf')
        bottom = matrix[row + 1][max_col] if row + 1 < ROWS else float('-inf')
        
        if value >= top and value >= bottom:
            return value
        elif value < top:
            right = row - 1
        else:
            left = row + 1
                
    return [-1, -1]

print(func(matrix))

"""
Problem Statement: Given a 0-indexed n x m matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the array [i, j]. A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbours to the left, right, top, and bottom.
Assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

Note: As there can be many peak values, 1 is given as output if the returned index is a peak number, otherwise 0.

OPTIMAL:
- find peak element in the row, then check above and below
    - utilize if else for out of bounds conditions
"""
