from itertools import permutations
from collections import defaultdict
import math

# matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16], [10, 13, 14, 17]]
s = "babad"
def expand_around_center(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    
    return l + 1, r - 1

def func(s):
    best_l, best_r = 0, 0
    
    for i in range(len(s)):
        l1, r1 = expand_around_center(s, i, i)
        l2, r2 = expand_around_center(s, i, i + 1)
        
        if r1 - l1 > best_r - best_l:
            best_l, best_r = l1, r1
        
        if r2 - l2 > best_r - best_l:
            best_l, best_r = l2, r2
        
    return s[best_l:best_r + 1]

print(func(s))

"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""
