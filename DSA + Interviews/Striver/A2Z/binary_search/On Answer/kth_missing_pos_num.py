from itertools import permutations
import math

arr = [4, 7, 9, 10]
k = 1

def calc_num_missing(arr, average):
    return arr[average] - (average + 1)

def func(arr, k):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        average = (left + right) // 2
        if calc_num_missing(arr, average) < k:
            left = average + 1
        else:
            right = average - 1
    
    return arr[right] + (k - calc_num_missing(arr, right))
        
print(func(arr, k))

"""
Problem Statement: You are given a strictly increasing array 'vec' and a positive integer 'k'. Find the 'kth' positive integer missing from 'vec'.

Example 1:
Input Format: vec[]={4,7,9,10}, k = 1
Result: 1
Explanation: The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 1, the first missing element is 1.

Example 2:
Input Format: vec[]={4,7,9,10}, k = 4
Result: 5
Explanation: The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 4, the fourth missing element is 5.

BF:
- count through all numbers 1 through max(arr)
- whenever a missing number pops up after check, increment a counter
- if counter hits k, return that value

OPTIMAL:
- binary search
- we want to shrink the search space to have left and right cross where right ends up at the starting point we want to start counting. we then add (k - missing numbers up to right pointer)
"""
