from itertools import permutations
import math

s = "(1+(2*3)+((8)/4))+1"

def func(s):
    count = 0
    max_depth = 0
    
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            
        max_depth = max(max_depth, count)
        
    return max_depth

print(func(s))

"""
OPTIMAL:
- keep a count of parenthesis - opening (+1), closing (-1) so that we can accurately tell where we are level wise

Problem Statement: Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

Example 1:
Input:
 s = "(1+(2*3)+((8)/4))+1"
Output:
 3
Explanation:
 Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input:
 s = "(1)+((2))+(((3)))"
Output:
 3
Explanation:
 Digit 3 is inside of 3 nested parentheses in the string.
"""
