from itertools import permutations
import math

s = "((()))"

def func(s):
    result = []
    count = 0
    
    for char in s:
        if char == '(':
            if count > 0:
                result.append(char)
            count += 1
        elif char == ')':
            count -= 1
            if count > 0:
                result.append(char)
        
    return ''.join(result)
    
print(func(s))

"""
Problem Statement: A valid parentheses string is defined by the following rules:

It is the empty string "".
If A is a valid parentheses string, then so is "(" + A + ")".
If A and B are valid parentheses strings, then A + B is also valid.

A primitive valid parentheses string is a non-empty valid string that cannot be split into two or more non-empty valid parentheses strings.

Given a valid parentheses string s, your task is to remove the outermost parentheses from every primitive component of s and return the resulting string.

OPTIMAL:
- we're given a valid parenthesis, which means we just have to check where the sets of valid parenthesis starts and ends
    - we will basically cut off whenever its at 1, both adding and removing
"""
