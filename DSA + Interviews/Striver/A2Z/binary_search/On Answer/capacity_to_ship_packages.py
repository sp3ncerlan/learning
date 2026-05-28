from itertools import permutations
import math

arr = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5

def daysNeeded(arr, capacity):
    days = 1
    current_weight = 0
    
    for weight in arr:
        if current_weight + weight > capacity:
            days += 1
            current_weight = weight
        else:
            current_weight += weight

    return days

def shipWithinDays(arr, d):
    left, right = max(arr), sum(arr)
    
    result = -1
    while left <= right:
        capacity = (left + right) // 2
        
        if daysNeeded(arr, capacity) <= d:
            result = capacity
            right = capacity - 1
        else:
            left = capacity + 1

    return result
        
print(shipWithinDays(arr, d))

"""
BF:
- try each number of capacities until we can group them in at most 'd' days
- o(sum(arr) - max(arr) * n), o(1)

OPTIMAL:
- configure shipWithinDays to use binary search instead
- o(n * log(sum(arr) - max(arr))), o(1)
"""
