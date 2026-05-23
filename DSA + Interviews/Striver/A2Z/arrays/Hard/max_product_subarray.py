"""
Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.

Input: Nums = [1,2,3,4,5,0]
Output: 120
Explanation: 
In the given array, 1x2x3x4x5 gives maximum product value.

Input: Nums = [1,2,-3,0,-4,-5]
Output: 20
Explanation: 
In the given array, (-4)x(-5) gives maximum product value.
"""
nums = [1,2,3,4,5,0]

def func(nums):
    if len(nums) == 0:
        return 0
    
    maximum = nums[0]
    
    # prefix fill
    prefix = 1
    for i in range(len(nums)):
        if nums[i] != 0:
            prefix = prefix * nums[i]
            maximum = max(maximum, prefix)
        else:
            prefix = 1
        
    # suffix fill
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != 0:
            suffix = suffix * nums[i]
            maximum = max(maximum, suffix)
        else:
            suffix = 1
        
    return maximum

print(func(nums))
