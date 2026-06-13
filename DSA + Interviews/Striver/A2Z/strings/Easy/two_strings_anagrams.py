from itertools import permutations
import math

s = "CAT"
t = "ACT"

def func(s, t):
    n, m = len(s), len(t)
    
    if n != m:
        return False
    
    freq = [0] * 26
    
    for char in s:
        freq[ord(char) - ord('A')] += 1
    
    for char in t:
        freq[ord(char) - ord('A')] -= 1
    
    for count in freq:
        if count != 0:
            return False
    
    return True

print(func(s, t))

"""
Problem Statement: Given two strings, check if two strings are anagrams of each other or not.

Example 1:
Input: CAT, ACT
Output: true
Explanation: Since the count of every letter of both strings are equal.

Example 2:
Input: RULES, LESRT 
Output: false
Explanation: Since the count of U and T  is not equal in both strings.
"""
