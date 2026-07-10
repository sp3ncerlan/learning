nums = [4, 2, 10, 5, 1, 3]
k = 5

def recurse(nums, start, total, target):
    if total == target:
        return 1
    
    if total > target:
        return 0
    
    result = 0
    for i in range(start, len(nums)):
        result += recurse(nums, i + 1, total + nums[i], target)

    return result
    
def func(nums, k):
    return recurse(nums, 0, 0, k)

print(func(nums, k))

"""
OPTIMAL:
- we can use include or exclude, and at each point check what adding both would give
- our base case should check if it equals the sum and add to result if so. if its greater, just return to prune the branch

Problem Statement: Given an array nums and an integer k.Return the number of non-empty subsequences of nums such that the sum of all elements in the subsequence is equal to k.

Example 1:
Input :
 nums = [4, 9, 2, 5, 1] , k = 10
Output :
 2
Explanation :
 The possible subsets with sum k are [9, 1] , [4, 5, 1].

Example 2:
Input :
 nums = [4, 2, 10, 5, 1, 3] , k = 5
Output :
 3
Explanation :
 The possible subsets with sum k are [4, 1] , [2, 3] , [5].
"""
