from itertools import permutations
import math

s = "paper"
t = "title"

def func(s, t):
    a1, a2 = [-1] * 256, [-1] * 256
    
    n = len(s)
    
    for i in range(n):
        if a1[ord(s[i])] != a2[ord(t[i])]:
            return False

        a1[ord(s[i])] = i
        a2[ord(t[i])] = i
        
    return True

print(func(s, t))

"""
OPTIMAL:
- use a dictionary and add the connections - if it exists, then a mapping exists and it is not valid

Problem Statement: Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1
Input:
 s = "paper", t = "title"
Output:
 true
Explanation:
 The characters in "s" can be mapped one-to-one to characters in "t": 
'p' → 't', 'a' → 'i', 'e' → 'l', 'r' → 'e'
Since the mapping is consistent and unique for each character, the strings are isomorphic.

Example 2
Input:
 s = "foo", t = "bar"
Output:
 false
Explanation:
 'f' → 'b' is fine, 'o' → 'a' for the first 'o', But the second 'o' in "s" would need to map to 'r' in "t", which conflicts with the earlier mapping of 'o' → 'a'
This inconsistency makes it impossible to convert "s" to "t" using a one-to-one character mapping.
"""
