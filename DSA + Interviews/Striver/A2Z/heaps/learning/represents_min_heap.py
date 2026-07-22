nums = [10, 20, 30, 21, 23]

def func(nums):
    n = len(nums)
    
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and nums[i] > nums[left]:
            return False
        
        if right < n and nums[i] > nums[right]:
            return False

    return True

print(func(nums))

"""
Problem Statement: Given an array of integers nums. Check whether the array represents a binary min-heap or not. Return true if it does, otherwise return false.
A binary min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is recursively true for all nodes in a Binary Tree.
"""
