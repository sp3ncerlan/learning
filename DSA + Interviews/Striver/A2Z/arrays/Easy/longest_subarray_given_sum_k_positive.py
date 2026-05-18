"""
Problem Statement: Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.

Example 1:
Input:
 nums = [10, 5, 2, 7, 1, 9], k = 15  
Output:
 4  
Explanation:
 The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

Example 2:
Input:
 nums = [-3, 2, 1], k = 6  
Output:
 0  
Explanation:
 There is no sub-array in the array that sums to 6. Therefore, the output is 0.     
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
