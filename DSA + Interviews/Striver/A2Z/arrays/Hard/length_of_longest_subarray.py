"""
Problem Statement: Given an array containing both positive and negative integers, we have to find the length of the longest subarray with the sum of all elements equal to zero.

Example 1:
Input:
 N = 6, array[] = {9, -3, 3, -1, 6, -5}  
Result:
 5  
Explanation:
 The following subarrays sum to zero:
- {-3, 3}
- {-1, 6, -5}
- {-3, 3, -1, 6, -5}
The length of the longest subarray with sum zero is 5.

Example 2:
Input:
 N = 8, array[] = {6, -2, 2, -8, 1, 7, 4, -10}  
Result:
 8  
Explanation:
 Subarrays with sum zero:
- {-2, 2}
- {-8, 1, 7}
- {-2, 2, -8, 1, 7}
- {6, -2, 2, -8, 1, 7, 4, -10}
The length of the longest subarray with sum zero is 8.

BF:
- we have to keep subarrays
- start at each subarray and check if its sum = 0 -> O(n^3)
    - update max global
- better yet, keep a running sum and make it O(n^2)
- space is O(1)

OPTIMAL:
- prefix sum -> insert each sum into hashmap
- check for existing sum in hashmap
    - if we see the same sum, the length between equals out to 0
    - update max
- if 0, update max as well
"""
from collections import defaultdict

nums = [6, -2, 2, -8, 1, 7, 4, -10]
n = 6

def func(nums):
    mpp = defaultdict(int)
    
    running_sum = 0
    maximum = 0
    for i, num in enumerate(nums):
        running_sum += num
        
        if running_sum == 0:
            maximum = i + 1
        else:
            if running_sum in mpp:
                maximum = max(maximum, i - mpp[running_sum])
            else:
                mpp[running_sum] = i
    
    return maximum

print(func(nums))
