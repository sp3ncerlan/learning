nums = [10, 1, 2, 7, 6, 1, 5]
target = 8

def recurse(nums, target, result, path, total, start):
    if total >= target:
        if total == target:
            result.append(path[:])
        return
    
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
            continue
        
        path.append(nums[i])
        recurse(nums, target, result, path, total + nums[i], i + 1)
        path.pop()
    
def func(nums, target):
    nums.sort()
    
    result = []
    path = []
    
    recurse(nums, target, result, path, 0, 0)
    
    return result

print(func(nums, target))

"""
Problem Statement: Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target. Each number in candidates may only be used once in the combination..

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]]
Explanation: These are the unique combinations whose sum is equal to target.
 
Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
Explanation: These are the unique combinations whose sum is equal to target.
        
"""
