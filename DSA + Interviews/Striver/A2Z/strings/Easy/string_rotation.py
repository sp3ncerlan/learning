from itertools import permutations
import math

s = "rotation"
goal = "tionrota"

# def func(s, goal):
#     n = len(s)
    
#     for i in range(n):
#         rotation = s[i:] + s[:i]
#         print(rotation)
        
#         if rotation == goal:
#             return True

#     return False

def func(s, goal):
    new_string = s * 2
    
    if goal in new_string:
        return True

    return False

print(func(s, goal))

"""
BF:
- o(n^2), o(n) for creation of each string and comparison and then storing

Problem Statement: Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position. For example, if s = "abcde", then it will be "bcdea" after one shift.

Example 1:
Input:
 s = "rotation", goal = "tionrota"
Output:
 true
Explanation:
 After multiple left shifts on "rotation", we get:
    1st shift → "otationr"
    2nd shift → "tationro"
    3rd shift → "ationrot"
    4th shift → "tionrota"
    So the goal string can be obtained by rotating the original string.

Example 2:
Input:
 s = "hello", goal = "lohelx"
Output:
 false
Explanation:
 
Even after all possible rotations of "hello", we cannot form "lohelx" due to the presence of an extra character 'x'. Hence, it's not possible.
"""
