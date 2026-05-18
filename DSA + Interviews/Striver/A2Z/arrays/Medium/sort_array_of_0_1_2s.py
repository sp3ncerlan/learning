"""
Problem Statement: Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.

Input: nums = [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]
Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two

Input: nums = [0, 0, 1, 1, 1]
Output: [0, 0, 1, 1, 1]
Explanation: The nums array in sorted order has 2 zeroes, 3 ones and zero twos.

BRUTE FORCE:
- Sort the array, which would make it 0 -> 1 -> 2
- O(nlogn), O(1)

BETTER:
- Count the number of 0s, 1s and 2s and then repopulate original array overwriting with the counts and nums
- O(n), O(1)

OPTIMAL:
Dutch flag
- low, med, high
- swap 0 to low, 2 to high, and continue on 1
- when swapping with high, keep pointer at mid since new num can be unsorted
- left of mid is sorted
"""

def dutch_flag(arr) -> int:
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1
            
    return arr

arr = [1, 0, 2, 1, 0]

print(dutch_flag(arr))
