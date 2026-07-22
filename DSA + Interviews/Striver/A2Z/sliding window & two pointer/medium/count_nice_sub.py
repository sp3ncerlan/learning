nums = [1, 1, 2, 1, 1]
k = 3

def helper(nums, k):
    odd_count = 0
    count = 0
    
    left = 0
    for right in range(len(nums)):
        right_num = nums[right]
        
        if right_num % 2 == 1:
            odd_count += 1
            
        while odd_count > k:
            left_num = nums[left]
            if left_num % 2 == 1:
                odd_count -= 1
            left += 1
            
        # calc
        count += (right - left + 1)
        
    return count

def func(nums, k):
    return helper(nums, k) - helper(nums, k - 1)

print(func(nums, k))

"""
Better approach:
- sliding window with odd number count
- if odd number count > k, then we shrink until no longer the case
    - each time we move left, we check if the number was an odd one and update odd count

optimal:
- atMost(k) - atMost(k - 1), since we want all the ways to sum up to only k, so we take all the ways up to k and then subtract the ways to k - 1

Problem Statement: Given an array nums and an integer k. An array is called nice if and only if it contains k odd numbers. Find the number of nice subarrays in the given array nums. A subarray is continuous part of the array.

Input :nums = [1, 1, 2, 1, 1] , k = 3
Output :2
Explanation :The subarrays with three odd numbers are [1, 1, 2, 1] [1, 2, 1, 1]

Input : nums = [4, 8, 2] , k = 1
Output :0
Explanation :The array does not contain any odd number.
"""
