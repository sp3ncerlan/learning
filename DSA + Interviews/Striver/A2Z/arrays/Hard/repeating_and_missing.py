"""
Problem Statement: Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.
Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.

Example 1:
Input:
 nums = [3, 5, 4, 1, 1]  
Output:
 [1, 2]  
Explanation:
 1 appears twice in the array, and 2 is missing from the array. So the output is [1, 2].

Example 2:
Input:
 nums = [1, 2, 3, 6, 7, 5, 7]  
Output:
 [7, 4]  
Explanation:
 7 appears twice in the array, and 4 is missing from the array. So the output is [7, 4].
 
BF:
- XOR? XORing a number by itself cancels it out to 0
"""

nums = [3, 5, 4, 1, 1]  

def findMissingRepeatingNumbers(nums):
    # XOR to find difference, then isolate
    xr = 0
    for num in nums:
        xr ^= num
    
    number = (xr & -xr)
    
    # number is our mask
    ones, zeros = 0, 0
    for num in nums:
        if (num & number) != 0:
            ones ^= num
        else:
            zeros ^= num
            
    for i in range(1, len(nums) + 1):
        if (i & number) != 0:
            ones ^= i
        else:
            zeros ^= i
    
    # check which one has duplicate
    count = 0
    for num in nums:
        if num == ones:
            count += 1
    
    # index 0 appears twice, index 1 is missing
    if count == 2:
        return [ones, zeros]
    
    return [zeros, ones]
    
print(findMissingRepeatingNumbers(nums))
