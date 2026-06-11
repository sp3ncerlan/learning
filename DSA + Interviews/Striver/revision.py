from itertools import permutations
import math

arr = [3,5,1]
k = 3

def stations_placed(arr, chosen_distance):
    stations = 0
    
    
    return splits
    
def func(arr, k):
    left, right = max(arr), sum(arr)
    
    optimal = -1
    while left <= right:
        chosen_distance = (left + right) // 2
        
        if stations_placed(arr, chosen_distance) <= k:
            optimal = chosen_distance
            right = chosen_distance - 1
        else:
            left = chosen_distance + 1
            
    return optimal

print(func(arr, k))

"""

"""
