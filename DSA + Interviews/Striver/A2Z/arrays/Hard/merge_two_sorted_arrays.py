"""
Problem Statement: Given two sorted integer arrays nums1 and nums2, merge both the arrays into a single array sorted in non-decreasing order.
The final sorted array should be stored inside the array nums1 and it should be done in-place.
Array nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s whereas nums2 has a length of n.

Input : nums1 = [-5, -2, 4, 5, 0, 0, 0], nums2 = [-3, 1, 8]
Output : [-5, -3, -2, 1, 4, 5, 8]
Explanation : The merged array is: [-5, -3, -2, 1, 4, 5, 8], where [-5, -2, 4, 5] are from nums1 and [-3, 1, 8] are from nums2

Input : nums1 = [0, 2, 7, 8, 0, 0, 0], nums2 = [-7, -3, -1]
Output :  [-7, -3, -1, 0, 2, 7, 8]
Explanation :  The merged array is: [-7, -3, -1, 0, 2, 7, 8], where [0, 2, 7, 8] are from nums1 and [-7, -3, -1] are from nums2

APPROACH:
- need three pointers
    - one starts from the back of nums1 to insert
    - one starts from the valid nums (not zero) from nums1 back
    - one starts from the valid nums (not zero) from nums2 back
    
- O(n + m), O(1) in place
"""

nums1, nums2 = [-3, -1, 0, 0, 0, 0], [-3, 1, 8]

def func(nums1, m, nums2, n):
    ptr1 = m - 1
    ptr2 = n - 1
    place = m + n - 1
    
    while ptr1 >= 0 and ptr2 >= 0:
        if nums1[ptr1] > nums2[ptr2]:
            nums1[place] = nums1[ptr1]
            ptr1 -= 1
        else:
            nums1[place] = nums2[ptr2]
            ptr2 -= 1
        
        place -= 1
    
    while ptr2 >= 0:
        nums1[place] = nums2[ptr2]
        ptr2 -= 1
        place -= 1
    
    return nums1
    
print(func(nums1, 3, nums2, 3))
