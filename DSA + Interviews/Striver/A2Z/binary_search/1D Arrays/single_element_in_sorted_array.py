"""
Problem Statement: Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.

Input : arr[] = {1,1,2,2,3,3,4,5,5,6,6}
Output: 4
Explanation: Only the number 4 appears once in the array.

Input: arr[] = {1,1,3,5,5}
Output : 3
Explanation: Only the number 3 appears once in the array.
"""
nums = [1,1,2,3,3,4,4,5,5,6,6]

def search(nums):
    n = len(nums)
    
    if n == 1:
        return nums[0]
    
    if nums[0] != nums[1]:
        return nums[0]

    if nums[n - 1] != nums[n - 2]:
        return nums[n - 1]
    
    left, right = 1, n - 2
    
    while left <= right:
        mid = (left + right) // 2
        
        if mid % 2 != 0:
            if nums[mid - 1] == nums[mid]: # correct
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[mid] == nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
    
    return nums[left]

print(search(nums))
