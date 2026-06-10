from itertools import permutations
import math

arr = [1, 2, 3, 4, 5]
d = 2

def days_for_weight(arr, weight):
    days = 1
    current_weight = 0
    for w in arr:
        if current_weight + w > weight:
            days += 1
            current_weight = w
        else:
            current_weight += w
    
    return days
    
def func(arr, d):
    left, right = max(arr), sum(arr)
    
    optimal = -1
    while left <= right:
        weight = (left + right) // 2
        
        if days_for_weight(arr, weight) <= d:
            optimal = weight
            right = weight - 1
        else:
            left = weight + 1
    
    return optimal

print(func(arr, d))

"""
BF:
- count each freq in a hashmap and then find the one that appears once (freq == 1)
- o(n), o(n)

OPTIMAL:
- 
"""
