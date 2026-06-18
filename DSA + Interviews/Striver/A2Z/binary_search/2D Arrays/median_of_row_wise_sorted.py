from itertools import permutations
import math

matrix = [[1, 3, 8], [2, 3, 4], [1, 2, 5]]

def count_values(matrix, target):
    count = 0

    for row in range(len(matrix)):
        left, right = 0, len(matrix[0]) - 1
        target_index = -1
        
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] <= target:
                target_index = mid
                left = mid + 1
            else:
                right = mid - 1
        
        if target_index != -1:
            count += (target_index + 1)
    
    return count

def func(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    
    left, right = float('inf'), float('-inf')
    for row in range(ROWS):
        if matrix[row][0] < left:
            left = matrix[row][0]
        
        if matrix[row][COLS - 1] > right:
            right = matrix[row][COLS - 1]
    
    half_count = (ROWS * COLS + 1) // 2
    optimal = -1
    while left <= right:
        mid = (left + right) // 2
        
        values_less_than = count_values(matrix, mid)
        if values_less_than >= half_count:
            optimal = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return optimal

print(func(matrix))

"""
Problem Statement:
Given a row-wise sorted matrix of size M*N, where M is no. of rows and N is no. of columns, find the median in the given matrix.
Note: M*N is odd.

OPTIMAL:
- two binary search, one nested
    - binary search on the values min(arr) through max(arr)
    - within the binary search, check the counts of values for each row by binary searching upper bound and try to count half
    - if half, then return the median
"""
