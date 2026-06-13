from itertools import permutations
import math

s = "0214638"

def func(s):
    first, last = -1, -1
    
    # find last odd num
    for i in range(len(s) - 1, -1, -1):
        if int(s[i]) % 2 == 1:
            last = i
            break
    
    # find first num
    for i in range(len(s)):
        if int(s[i]) > 0:
            first = i
            break
        
    return s[first:last + 1]

print(func(s))

"""
Problem Statement: Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.
The number returned should not have leading zero's. But the given input string may have leading zero.

OPTIMAL:
- start from back, find the first odd number
- find the first valid number
- this subarray is the longest
"""
