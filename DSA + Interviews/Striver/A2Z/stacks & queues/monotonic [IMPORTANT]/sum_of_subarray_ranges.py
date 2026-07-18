nums = [1, 2, 3]

def findNSE(nums):
    n = len(nums)
    stack = []
    ans = [0] * n
    
    for i in range(n - 1, -1, -1):
        num = nums[i]
        
        while stack and nums[stack[-1]] >= num:
            stack.pop()

        ans[i] = stack[-1] if stack else n
        
        stack.append(i)
        
    return ans
    
def findPSEE(nums):
    n = len(nums)
    stack = []
    ans = [0] * n
    
    for i in range(n):
        num = nums[i]
        
        while stack and nums[stack[-1]] > num:
            stack.pop()
            
        ans[i] = stack[-1] if stack else -1
        
        stack.append(i)
        
    return ans
    
def findNGE(nums):
    n = len(nums)
    stack = []
    ans = [0] * n
    
    for i in range(n - 1, -1, -1):
        num = nums[i]
        
        while stack and nums[stack[-1]] <= num:
            stack.pop()
            
        ans[i] = stack[-1] if stack else n
        
        stack.append(i)
        
    return ans
    
def findPGEE(nums):
    n = len(nums)
    stack = []
    ans = [0] * n
    
    for i in range(n):
        num = nums[i]
        
        while stack and nums[stack[-1]] < num:
            stack.pop()
            
        ans[i] = stack[-1] if stack else -1
        
        stack.append(i)
        
    return ans

def sumSubarrayMin(nums):
    n = len(nums)
    
    nse = findNSE(nums)
    psee = findPSEE(nums)
    
    total = 0
    for i in range(n):
        left = i - psee[i]
        right = nse[i] - i
        
        freq = left * right * 1
        val = (freq * nums[i] * 1)
        
        total += val
        
    return total

def sumSubarrayMax(nums):
    n = len(nums)
    
    nge = findNGE(nums)
    pgee = findPGEE(nums)
    
    total = 0
    for i in range(n):
        left = i - pgee[i]
        right = nge[i] - i
        
        freq = left * right * 1
        val = (freq * nums[i] * 1)
        
        total += val
        
    return total
    
def func(nums):
    return sumSubarrayMax(nums) - sumSubarrayMin(nums)

print(func(nums))

"""
Problem Statement: Given an integer array nums, determine the range of a subarray, defined as the difference between the largest and smallest elements within the subarray. Calculate and return the sum of all subarray ranges of nums.

A subarray is defined as a contiguous, non-empty sequence of elements within the array.

Example 1:
Input:
 nums = [1, 2, 3]
Output:
 4
Explanation:
 The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

Example 2:
Input:
 nums = [1, 3, 3]
Output:
 4
Explanation:
 The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
"""
