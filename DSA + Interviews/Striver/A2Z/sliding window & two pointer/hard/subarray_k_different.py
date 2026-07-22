nums = [1, 2, 1, 3, 4]
k = 3

def helper(nums, k):
    freq = {}
    subarrays = 0
    left = 0
    
    for right in range(len(nums)):
        freq[nums[right]] = freq.get(nums[right], 0) + 1
        
        while len(freq) > k:
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1
        
        # calc
        subarrays += (right - left + 1)
        
    return subarrays
                            
def func(nums, k):
    return helper(nums, k) - helper(nums, k - 1)

print(func(nums, k))

"""
Optimal:
- hashmap with freq, keep size k or under

Problem Statement: You are given an integer array nums and an integer k. Return the number of good subarrays of nums.

A good subarray is defined as a contiguous subarray of nums that contains exactly k distinct integers. A subarray is a contiguous part of the array.

Input: nums = [1, 2, 1, 2, 3], k = 2  
Output: 7
Explanation: The 7 subarrays with exactly 2 different integers are:
[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]


Input: nums = [1, 2, 1, 3, 4], k = 3  
Output: 3
Explanation: The 3 subarrays with exactly 3 different integers are:  
[1,2,1,3], [2,1,3], [1,3,4] 
"""
