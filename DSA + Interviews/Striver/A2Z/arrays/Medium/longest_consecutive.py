"""
Problem Statement: Given an array nums of n integers.

Return the length of the longest sequence of consecutive integers. The integers in this sequence can appear in any order.

Example 1:
Input:
 nums = [100, 4, 200, 1, 3, 2]  
Output:
 4  
Explanation:
 The longest sequence of consecutive elements in the array is [1, 2, 3, 4], which has a length of 4. This sequence can be formed regardless of the initial order of the elements in the array.

Example 2:
Input:
 nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  
Output:
 9  
Explanation:
 The longest sequence of consecutive elements in the array is [0, 1, 2, 3, 4, 5, 6, 7, 8], which has a length of 9.
 
BRUTE FORCE:
- start at each number and check if the next one exists, if so then increment length and continue (linear search)
- O(n^2), O(1)
 
BETTER:
- sort in ascending order, groups consecutive numbers together
- use a lastSmaller to keep track of the last number seen, and then skip duplicates using condition
- log a longest variable tracking the longest consec sequence
- O(nlogn) due to sorting, O(1)

OPTIMAL:
- current length and longest so far variables
- convert to a set for O(1) lookup
- check if num - 1 is in the set, if not then its start of a sequence
- check if num + 1 in the set, then increment num and check again, until no more consecutive exists and update longest on each iteration
- O(n), O(n) for set
"""

# def longest_consecutive(nums) -> int:
#     lastSmaller = float('-inf')
    
#     nums.sort()
    
#     longest = 1
#     current_length = 0
#     for num in nums:
#         if num == lastSmaller + 1:
#             current_length += 1
#             lastSmaller = num
#         elif num != lastSmaller:
#             lastSmaller = num
#             current_length = 1
            
#         longest = max(longest, current_length)
        
#     return longest

def longest_consecutive(nums) -> int:
    if not nums:
        return 0
    
    longest = 1
    nums = set(nums)
    
    for current_num in nums:
        if current_num - 1 not in nums:
            current_length = 1
            # start of new seq
            while current_num + 1 in nums:
                current_num += 1
                current_length += 1
                
            longest = max(longest, current_length)
            
    return longest

nums = [100, 4, 200, 1, 3, 2]

print(longest_consecutive(nums))
