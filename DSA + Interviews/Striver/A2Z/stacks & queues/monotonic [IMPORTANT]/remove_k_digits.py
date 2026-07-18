nums = "1002991"
k = 2

# save numbers we've removed, if they match then we can remove them again

"""
"1002991"

stack = [0, 0, 2, 1]
"""
    
def func(nums, k):
    stack = []
    n = len(nums)
    
    for i in range(n):
        while stack and stack[-1] > nums[i] and k > 0:
            stack.pop()
            k -= 1
            
        stack.append(nums[i])
        
    while k > 0:
        stack.pop()
        k -= 1
        
    result = "".join(stack)
    
    return result.lstrip('0')

print(func(nums, k))

"""
Problem Statement: Given a string nums representing a non-negative integer, and an integer k, find the smallest possible integer after removing k digits from num.

Example 1:
Input:
 nums = "541892", k = 2
Output:
 "1892"
Explanation:
 Removing the two digits 5 and 4 yields the smallest number, 1892.

Example 2:
Input:
 nums = "1002991", k = 3
Output:
 "21"
Explanation:
 Remove the three digits 1(leading one), 9, and 9 to form the new number 21(Note that the output must not contain leading zeroes) which is the smallest.
"""
