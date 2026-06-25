from itertools import permutations
from collections import defaultdict
import math
import bisect

# matrix = [[1, 4, 9], [2, 5, 6], [3, 8, 7]]
# arr1 = [1, 2]
# arr2 = [3, 4]
# k =
# s = " amazing coding skills "
# t = "bar"
arr = [4, 7, 9, 10]
k = 4

def func(arr, k):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        check = (left + right) // 2
        diff = arr[check] - (check + 1)
        
        if diff < k:
            left = check + 1
        else:
            right = check - 1
    
    return left + k

print(func(arr, k))

"""
OPTIMAL:
- binary search to find the current diff between the number that should be there and the number that is actually there
- using the difference
    - if the diff is <= k, it means that the number is there are less missing numbers than needed
        - we'll check right to increase the number of missing numbers possible
- once the left and right cross, the answer is between the right and left pointers
- it would be right + (number needed (k) - number of missing numbers on the left)
"""
