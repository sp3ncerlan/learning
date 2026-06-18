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
