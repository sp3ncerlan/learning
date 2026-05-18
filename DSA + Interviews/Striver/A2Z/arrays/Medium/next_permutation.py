"""
Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

Input: Arr[] = {1,3,2}
Output: {2,1,3}
Explanation: All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,13} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2} is {2,1,3}.

Input : Arr[] = {3,2,1}
Output: {1,2,3}
Explanation : As we see all permutations of {1,2,3}, we find {3,2,1} at the last position. So, we have to return the lowest permutation.

BRUTE FORCE:
- grab all permutations (itertools permutations)
- sort them
- find the current permutation in the sorted list, then return the one after it or the first one if it is the last in the sorted list
- O(N! * N) since generating permutations (N!), space is O(N!) for storing perms

OPTIMAL:
- traverse from end and find first index where current digit is smaller than the next one (breaking point)
- traverse again from the end to find the first greater than the breaking point digit and swap
- reverse portion of array to the right of the breaking point to get smallest next perm
- if no such breaking point, just reverse entire array
- O(n), O(1)
"""

# from itertools import permutations

# def next_permutation(arr) -> int:
#     perms = sorted(set(permutations(arr)))
    
#     current = tuple(arr)
    
#     for i in range(len(perms)):
#         if perms[i] == current:
#             if i == len(perms) - 1:
#                 return list(perms[0])
#             return list(perms[i + 1])
    
#     return arr

def next_permutation(nums) -> int:
    index = -1
    
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            index = i
            break
            
    # check if there even is a breakpoint
    if index == -1:
        nums.reverse()
        return nums
            
    for i in range(len(nums) - 1, index, -1):
        if nums[i] > nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
            break

    # reverse
    nums[index + 1:] = reversed(nums[index + 1:])
    
    return nums

nums = [1, 3, 2]

print(next_permutation(nums))
