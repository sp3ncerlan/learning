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
"""

def longest_subarray_given_sum_k(arr, k) -> int:
    left = 0
    longest_sub = 0
    current_sum = 0
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while left <= right and current_sum > k:
            current_sum -= arr[left]
            left += 1
        
        if current_sum == k:
            longest_sub = max(longest_sub, right - left + 1)
    
    return longest_sub

arr = [10, 5, 2, 7, 1, 9]
k = 15

print(longest_subarray_given_sum_k(arr, k))
