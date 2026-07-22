s = "abcba"

def func(s):
    last_seen = {'a': -1, 'b': -1, 'c': -1}
    substrings = 0
    
    left = 0
    for right in range(len(s)):
        right_char = s[right]
        last_seen[right_char] = right
        
        if -1 not in last_seen.values():
            substrings += (min(last_seen.values()) + 1)
        
    return substrings

print(func(s))

"""
Better approach:
- sliding window with hashmap
    - count always 3
- frequencies, while length of hashmap == 3, we add one to result

optimal:
- 

Problem Statement: Given a string s , consisting only of characters 'a' , 'b' , 'c'.Find the number of substrings that contain at least one occurrence of all these characters 'a' , 'b' , 'c'.

Input : s = "abcba"
Output :  5
Explanation : The substrings containing at least one occurrence of the characters 'a' , 'b' , 'c' are "abc" , "abcb" , "abcba" , "bcba" , "cba".


Input : s = "ccabcc"
Output : 8
Explanation : The substrings containing at least one occurrence of the characters 'a' , 'b' , 'c' are "ccab" , "ccabc" , "ccabcc" , "cab" , "cabc" , "cabcc" , "abc" , "abcc".
"""
