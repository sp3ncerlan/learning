s = "abcddefg"
k = 3

def func(s):
    freq = {}
    longest = 0
    
    left = 0
    for right in range(len(s)):
        right_char = s[right]
        freq[right_char] = freq.get(right_char, 0) + 1
        
        while len(freq) > k:
            left_char = s[left]
            freq[left_char] -= 1
            if freq[left_char] == 0:
                del freq[left_char]
            left += 1
            
        # calc
        longest = max(longest, (right - left + 1))
        
    return longest

print(func(s))

"""
Optimal:
- hashmap with freq, keep size k or under

Problem Statement: Given a string s and an integer k.Find the length of the longest substring with at most k distinct characters

Input :s = "aababbcaacc" , k = 2
Output :6
Explanation :The longest substring with at most two distinct characters is "aababb".
The length of the string 6


Input : s = "abcddefg" , k = 3
Output : 4
Explanation : The longest substring with at most three distinct characters is "bcdd".
The length of the string 4.
"""
