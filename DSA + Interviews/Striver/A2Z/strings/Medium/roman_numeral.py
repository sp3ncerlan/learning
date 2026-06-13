from itertools import permutations
import math

s = "LVIII"

def func(s):
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    
    result = 0
    
    for i, char in enumerate(s):
        if i != len(s) - 1:
            if (char == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X') or
                char == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C') or
                char == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M')):
                result -= roman_to_int[char]
            else:
                result += roman_to_int[char]
        else:
            result += roman_to_int[char]
            
    return result

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
