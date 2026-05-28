"""
Problem Statement:
Given an integer array arr of size N, sorted in ascending order (with distinct values), the array is rotated at any index which is unknown. Find the minimum element in the array.

Input: arr = [4,5,6,7,0,1,2,3]
Output: 0
Explanation: The minimum element in the array is 0.

Input : arr = [3,4,5,1,2]
Output: 1
Explanation : The minimum element in the array is 1.

BF:
- linear search for minimum

OPTIMAL:
- binary search
- check if mid > right, and if so, the pivot point is on the right
- else, pivot point on the left
"""
nums = [3, 4, 5, 1, 2]

def search(nums):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            # pivot point on right
            left = mid + 1
        else:
            right = mid - 1
    
    return nums[left]

print(search(nums))
