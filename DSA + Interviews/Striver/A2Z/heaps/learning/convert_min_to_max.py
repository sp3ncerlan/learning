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
Given a min-heap in array representation named nums, convert it into a max-heap and return the resulting array.



A min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is recursively true for all nodes in the Binary Tree.

A max-heap is a complete binary tree where the key at the root is the maximum among all keys present in a binary max-heap and the same property is recursively true for all nodes in the Binary Tree.



Since there can be multiple answers, the compiler will return true if it's correct, else false.
"""
