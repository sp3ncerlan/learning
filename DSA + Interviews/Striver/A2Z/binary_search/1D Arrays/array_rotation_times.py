"""
Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values). Now the array is rotated between 1 to N times which is unknown. Find how many times the array has been rotated.

Input : arr = [4,5,6,7,0,1,2,3]
Result: 4
Explanation: The original array should be [0,1,2,3,4,5,6,7]. So, we can notice that the array has been rotated 4 times.

Input : arr = [3,4,5,1,2]
Output : 3
Explanation: The original array should be [1,2,3,4,5]. So, we can notice that the array has been rotated 3 times.
"""
nums = [4,5,6,7,0,1,2,3]

def search(nums):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            # pivot point on right
            left = mid + 1
        else:
            right = mid - 1
    
    return left

print(search(nums))
