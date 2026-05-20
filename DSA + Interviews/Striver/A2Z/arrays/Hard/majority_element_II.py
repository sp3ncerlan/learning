"""
Problem Statement: Given an integer array nums of size n. Return all elements which appear more than n/3 times in the array. The output can be returned in any order.

Example 1:
Input:
 nums = [1, 2, 1, 1, 3, 2]  
Output:
 [1]  
Explanation:
 Here, n / 3 = 6 / 3 = 2.  
Therefore, the elements appearing 3 or more times are: [1].

Example 2:
Input:
 nums = [1, 2, 1, 1, 3, 2, 2]  
Output:
 [1, 2]  
Explanation:
 Here, n / 3 = 7 / 3 = 2.  
Therefore, the elements appearing 3 or more times are: [1, 2].

BRUTE FORCE:
- maybe sort first, then just count each number and see if the total freq is greater than n/3
"""

nums = [1, 2, 1, 1, 3, 2, 2]

def func(nums):
    el1, el2 = -1, -1
    cnt1, cnt2 = 0, 0
    
    for num in nums:
        if num == el1:
            cnt1 += 1
        elif num == el2:
            cnt2 += 1
        elif cnt1 == 0:
            el1, cnt1 = num, 1
        elif cnt2 == 0:
            el2, cnt2 = num, 1
        else:
            cnt1 -= 1
            cnt2 -= 1
        
    result = []
    boundary = len(nums) // 3
    if nums.count(el1) > boundary:
        result.append(el1)
    if nums.count(el2) > boundary and el1 != el2:
        result.append(el2)
        
    return result

# def func(nums):
#     unique_nums = set()
#     boundary = len(nums) // 3
    
#     result = []
#     for num in nums:
#         if num in unique_nums:
#             continue
            
#         unique_nums.add(num)
#         freq = nums.count(num)
        
#         if freq > boundary:
#             result.append(num)
        
#         if len(result) == 2:
#             break
    
#     return result if len(result) > 0 else -1

print(func(nums))
