"""
Problem Statement: You are given a 0-indexed array nums of length n representing your maximum jump capability from each index.

You start at index 0. Each element nums[i] represents the maximum number of steps you can jump forward from index i.
Your goal is to reach the last index of the array (nums[n - 1]) using the minimum number of jumps
Return the minimum number of jumps required to reach the last index.
You can assume that it is always possible to reach the last index.
"""
nums = [2, 3, 1, 1, 4]

def func(nums):
    farthest = 0
    current_end = 0
    jumps = 0

    for i in range(len(nums)):
        if i == current_end:
            jumps += 1
            current_end = farthest

        current_end = max(current_end, i + nums[i])

    return jumps

print(func(nums))
