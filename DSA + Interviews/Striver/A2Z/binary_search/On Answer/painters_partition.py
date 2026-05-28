arr = [10, 20, 30, 40]
k = 2

def calc_splits(arr, count):
    painters_needed = 1
    
    current_units = 0
    for units in arr:
        if current_units + units > count:
            painters_needed += 1
            current_units = units
        else:
            current_units += units
        
    return painters_needed

def func(arr, k):
    left, right = max(arr), sum(arr)
    
    optimal = left
    while left <= right:
        units = (left + right) // 2
        
        if calc_splits(arr, units) <= k:
            optimal = units
            right = units - 1
        else:
            left = units + 1
    
    return optimal
        
print(func(arr, k))

"""
Problem Statement: Given an array/list of length 'N', where the array/list represents the boards and each element of the given array/list represents the length of each board. Some 'K' numbers of painters are available to paint these boards. Consider that each unit of a board takes 1 unit of time to paint. You are supposed to return the area of the minimum time to get this job done of painting all the 'N' boards under the constraint that any painter will only paint the continuous sections of boards.

BF:
- bounds by time -> max(arr), sum(arr)
- helper method checks to see if we can partition for k

OPTIMAL:
"""
