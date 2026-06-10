from itertools import permutations
import math

nums1, nums2 = [100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892]
k = 7

"""
[2, 3, 6, 7, 9]
[1, 4, 8, 10]
"""

# def countPairs(arr, low, mid, high):
    
def func(nums1, nums2, k):
    n, m = len(nums1), len(nums2)
    
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    left, right = 0, n
    while left <= right:
        mid1 = (left + right) // 2 # 2
        mid2 = k - mid1
        
        l1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
        l2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
        
        r1 = nums1[mid1] if mid1 < n else float('inf')
        r2 = nums2[mid2] if mid2 < m else float('inf')
        
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            right = mid1 - 1
        else:
            left = mid1 + 1
            
    return -1

print(func(nums1, nums2, k))

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
