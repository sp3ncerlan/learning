from itertools import permutations
from collections import defaultdict
import math

# matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16], [10, 13, 14, 17]]
s = " amazing coding skills "

# def func(s):
#     result = []
#     word = []
#     for char in s:
#         if char != " ":
#             word.append(char)
#         else:
#             result.append("".join(word))
#             word = []
    
#     result.reverse()
#     return " ".join(result)

def func(s):
    result = []
    
    i = len(s) - 1
    while i >= 0:
        while i >= 0 and s[i] == " ":
            i -= 1
        
        if i < 0:
            break
        
        end = i
        
        while i >= 0 and s[i] != " ":
            i -= 1
        
        word = s[i + 1:end + 1]
        
        result.append(word)
        
    return " ".join(result)    

print(func(s))

"""
Problem Statement: Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). A word is defined as a sequence of non-space characters. The words in s are separated by at least one space. Return a string with the words in reverse order, concatenated by a single space.

Input: s = "welcome to the jungle"
Output: "jungle the to welcome"
Explanation: The words in the input string are "welcome", "to", "the", and "jungle". Reversing the order of these words gives "jungle", "the", "to", and "welcome". The output string should have exactly one space between each word.

Input: s = " amazing coding skills "
Output: "skills coding amazing"
Explanation: The input string has leading and trailing spaces, as well as multiple spaces between the words "amazing", "coding", and "skills". After trimming the leading and trailing spaces and reducing the multiple spaces between words to a single space, the words are "amazing", "coding", and "skills". Reversing the order of these words gives "skills", "coding", and "amazing". The output string should not have any leading or trailing spaces and should have exactly one space between each word.
"""

from itertools import permutations
import math

s = " amazing coding skills "

def func(s):
    words = []
    
    word = []
    
    for char in s:
        if char != " ":
            word.append(char)
        elif word:
            words.append(''.join(word))
            word = []
    
    if word:
        words.append(''.join(word))
        
    words.reverse()
    
    return " ".join(words)
    
print(func(s))

"""
Problem Statement: Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). A word is defined as a sequence of non-space characters. The words in s are separated by at least one space. Return a string with the words in reverse order, concatenated by a single space.

BF:
- break out the string into array of characters
- result array contains each character so far
- if the current character is a space and the previous char on top is a letter, then we append the space
    -otherwise, continue
"""
