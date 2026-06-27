from itertools import permutations
from collections import defaultdict
import math
import bisect

matrix = [[1, 4, 9], [2, 5, 6], [3, 8, 7]]
# arr1 = [1, 2]
# arr2 = [3, 4]
# k =
# s = "a car"
# t = "bar"
# arr = [1, 2, 3, 4, 5]
# k = 4

def get_count(row, median):
    return bisect.bisect_right(row, median)

def func(matrix):
    low, high = min(row[0] for row in matrix), max(row[-1] for row in matrix)
    
    target = (len(matrix) * len(matrix[0])) // 2
    
    while low <= high:
        median = (low + high) // 2
        
        count = 0
        for row in matrix:
            count += get_count(row, median)
        
        if count <= target:
            low = median + 1
        else:
            high = median - 1

    return low

print(func(matrix))

"""
OPTIMAL:
- we binary search on the min and max numbers in the matrix, then using that compare each line binary searching for the count
- we can get the count by doing bisect_right, which gives us the index where it should go. count would be that number
"""
