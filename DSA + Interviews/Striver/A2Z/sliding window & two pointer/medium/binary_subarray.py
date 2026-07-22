nums = [1, 0, 0, 1, 1, 0]
goal = 2

def func(nums, goal):
    freq = {0 : 1}
    total = 0
    sub_count = 0
    
    for i in range(len(nums)):
        total += nums[i]
        diff = total - goal
        
        if diff in freq:
            sub_count += freq[diff]
        
        freq[total] = freq.get(total, 0) + 1
        
    return sub_count

print(func(nums, goal))

"""
Better approach:
- sliding window with running totals, if number is a 1 then we subtract 1 from the total from left if > goal

optimal:
- atMost(k) - atMost(k - 1), since we want all the ways to sum up to only k, so we take all the ways up to k and then subtract the ways to k - 1

Problem Statement: You are given a binary array nums (containing only 0s and 1s) and an integer goal. Return the number of non-empty subarrays of nums that sum to goal. A subarray is a contiguous part of the array.

Input: nums = [1, 0, 0, 1, 1, 0], goal = 2  
Output: 6
Explanation: There are 6 subarrays with sum exactly equal to 2:
[1, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1], [1, 1], [1, 1, 0], [0,0,1,1,0]


Input: nums = [0,0,0,0,0,0], goal = 0  
Output: 21  
Explanation: All subarrays with only 0s will have sum = 0.  
There are 21 such subarrays in total (n(n+1)/2 = 6*7/2 = 21).
"""
