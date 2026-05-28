"""
Problem Statement: Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k is not present return -1.

Input:nums = [4, 5, 6, 7, 0, 1, 2], k = 0
Output :4
Explanation : Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

Input: nums = [4, 5, 6, 7, 0, 1, 2], k = 3
Output :-1
Explanation :Here, the target is 3. Since 3 is not present in the given rotated sorted array. Thus, we get the output as -1.

BF:
- linear search and find k, then return the index but if we end with index = -1, then we return it anyway
- o(n), o(1)

OPTIMAL:
- compare the mid to rightmost
    - if it is greater, then we know that the right side is not sorted
    - if it is less, then the right side is sorted
- we can use this to do binary search on the sorted halves and check if the target is in each section
- o(logn), o(1)
"""
nums = [4, 5, 6, 7, 0, 1, 2]
k = 3

def func(nums, k):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == k:
            return mid
        elif nums[mid] > nums[right]:
            # right side unsorted
            if nums[left] <= k < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # right side sorted
            if nums[mid] < k <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

print(func(nums, k))
