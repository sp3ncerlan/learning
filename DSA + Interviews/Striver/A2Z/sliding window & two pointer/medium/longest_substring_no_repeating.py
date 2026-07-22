s = "abcddabac"

def func(s):
    max_length = 0
    char_map = {}
    
    left = 0
    for right in range(len(s)):
        right_char = s[right]
        
        if right_char in char_map:
            left = max(char_map[right_char] + 1, left)
        
        char_map[right_char] = right
        
        # calc
        max_length = max(max_length, right - left + 1)
        
    return max_length

print(func(s))

"""
BF:
- iterate through all substrings, while maintaining a hash set on each iteration to see if we hit a repeated char
- o(n^2)

OPTIMAL:
- sliding window
- when we hit a char we've already seen, in a while loop, we will shrink until it is no longer the case
- once that happens, then we calculate length and update max length

Problem Statement: Given a string, S. Find the length of the longest substring without repeating characters.

Example 1:
Input:
 S = "abcddabac"  
Output:
 4  
Explanation:
 The longest substring with distinct characters is "abcd", which has a length of 4.

Example 2:
Input:
 S = "aaabbbccc"  
Output:
 2  
Explanation:
 The longest substrings with distinct characters are "ab" and "bc", both having a length of 2.
"""
