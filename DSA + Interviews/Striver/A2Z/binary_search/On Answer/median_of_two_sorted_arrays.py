from itertools import permutations
import math

nums1, nums2 = [1, 2], [3, 4]

"""
[1, 3, 6, 9]
[2, 4, 5, 7, 10]
"""

# def countPairs(arr, low, mid, high):
    
def func(nums1, nums2):
    n, m = len(nums1), len(nums2)
    
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    half = (n + m + 1) // 2 # 5
    left, right = 0, n
    while left <= right:
        mid1 = (left + right) // 2 # 2
        mid2 = half - mid1 # 3
        
        l1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
        l2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
        
        r1 = nums1[mid1] if mid1 < n else float('inf')
        r2 = nums2[mid2] if mid2 < m else float('inf')
        
        if l1 <= r2 and l2 <= r1:
            if (n + m) % 2 != 0:
                return float(max(l1, l2))
            else:
                return float(max(l1, l2) + min(r1, r2)) / 2.0
        elif l1 > r2:
            right = mid1 - 1
        else:
            left = mid1 + 1
            
    return 0.0

print(func(nums1, nums2))

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
