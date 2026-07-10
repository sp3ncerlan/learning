nums = [4, 3, 9, 2]
k = 10

def recurse(nums, start, total, target):
    if total == target:
        return True
    
    for i in range(start, len(nums)):
        if recurse(nums, i + 1, total + nums[i], target):
            return True
    
    return False
    
def func(nums, k):
    return recurse(nums, 0, 0, k)

print(func(nums, k))

"""
OPTIMAL:
- we can use include or exclude, and at each point check what adding both would give
- our base case should check if it equals the sum and add to result if so. if its greater, just return to prune the branch

Problem Statement: Given an array nums and an integer k. Return true if there exist subsequences such that the sum of all elements in subsequences is equal to k else false.

Example 1:
Input :
 nums = [1, 2, 3, 4, 5] , k = 8
Output :
 Yes
Explanation :
 The subsequences like [1, 2, 5] , [1, 3, 4] , [3, 5] sum up to 8.

Example 2:
Input :
 nums = [4, 3, 9, 2] , k = 10
Output :
 No
Explanation :
 No subsequence can sum up to 10.
"""
