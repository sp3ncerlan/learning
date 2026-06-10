from itertools import permutations
import math

matrix = [[0, 0, 0], [0, 0, 1], [0, 0, 0]]

def func(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    
    index = -1
    max_zero_count = 0
    for row in range(ROWS):
        left, right = 0, COLS - 1
        first_zero = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if matrix[row][mid] == 1:
                first_zero = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if first_zero != -1:
            zero_count = (COLS - first_zero)
            if zero_count > max_zero_count:
                max_zero_count = zero_count
                index = row
    
    return index

print(func(matrix))

"""
BF:
- check through m * n, find the row with the most 1s and return
- takes advantage of fact that its sorted asc

OPTIMAL:
- improve time complexity by doing a binary search on the row, finding first 1 and taking the count by doing (col count - (1st index 1 + 1))
- o(rows * log(cols))
"""
