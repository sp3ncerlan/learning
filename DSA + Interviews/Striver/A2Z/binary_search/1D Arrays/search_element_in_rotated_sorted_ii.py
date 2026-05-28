"""
Problem Statement: Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False.

Example 1:
Input Format: arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
Result: True
Explanation: The element 3 is present in the array. So, the answer is True.

Example 2:
Input Format: arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 10
Result: False
Explanation: The element 10 is not present in the array. So, the answer is False.

BF:
- linear search and find k, then return true but if we end without finding it, then we return false
- o(n), o(1)

OPTIMAL:
- binary search
- right side can be the same value as mid, then we don't know which side is sorted
- to combat this, we can shrink the array each time we find its the same on the right
- then we just do the same search
"""
nums = [3, 4, 3, 3, 1, 3]
k = 4

def search(nums, target) -> bool:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return True

        if nums[m] < nums[r]:  # Right portion
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
        elif nums[m] > nums[r]:  # Left portion
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            r -= 1

    return False

print(search(nums, k))
