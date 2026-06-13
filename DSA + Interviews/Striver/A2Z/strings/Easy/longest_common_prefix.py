from itertools import permutations
import math

str = ["flower", "flow", "flight"]

def func(str):
    str.sort() # flight, flow, flower
    
    first, last = str[0], str[-1]
    len_of_smallest = float('inf')
    for word in str:
        len_of_smallest = min(len_of_smallest, len(word))
    
    for i in range(len_of_smallest):
        if first[i] != last[i]:
            return first[:i]
        
    return first

print(func(str))

"""
Problem Statement: Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

Example 1
Input:
 str = ["flower", "flow", "flight"]
Output:
 "fl"
Explanation:
 All strings in the array begin with the common prefix "fl".

Example 2
Input:
 str = ["apple", "banana", "grape", "mango"]
Output:
 ""
Explanation:
 None of the strings share a common starting sequence, so the result is an empty string.
"""
