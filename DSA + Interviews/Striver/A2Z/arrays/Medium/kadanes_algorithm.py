"""
Problem Statement: Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input:
 nums = [2, 3, 5, -2, 7, -4]  
Output:
 15  
Explanation:
 The subarray from index 0 to index 4 has the largest sum = 15, which is the maximum sum of any contiguous subarray.

Example 2:
Input:
 nums = [-2, -3, -7, -2, -10, -4]  
Output:
 -2  
Explanation:
 The largest sum is -2, which comes from taking the element at index 0 or index 3 as the subarray. Since all numbers are negative, the subarray with the least negative number gives the largest sum.
 
 BRUTE FORCE:
 - check all substrings to see the sum and update global max sum
 - O(n^3), O(1)
 
 BETTER:
 - like brute force, but instead of calculating sum each time, we keep a current_sum inside the inner loop and add arr[j] to the sum as we expand
 - O(n^2), O(1)
 
 OPTIMAL:
 - keep track of a running sum
 - when the running sum turns negative, reset it to 0 to indicate we start a new subarray as negative subarrays don't contribute to maximum sums
 - update maximum sum if the current_sum is greater like usual
 - O(n), O(1)
"""

def kadane(arr) -> int:
    max_sum = float('-inf')
    
    current_sum = 0
    start = 0
    ans_start, ans_end = -1, -1
    for i, num in enumerate(arr):
        current_sum += num
        
        if current_sum > max_sum:
            max_sum = current_sum
            ans_start = start
            ans_end = i
        
        if current_sum < 0:
            current_sum = 0
            start = i + 1
            
    return arr[ans_start:ans_end + 1]

arr = [2, 3, 5, -2, 7, -4]

print(kadane(arr))
