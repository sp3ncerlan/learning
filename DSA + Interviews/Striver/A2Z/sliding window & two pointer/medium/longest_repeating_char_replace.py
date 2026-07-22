s = "AABABBA"
k = 1

def func(s, k):
    freq_map = {}
    max_freq = 0
    max_length = 0
    
    left = 0
    for right in range(len(s)):
        right_char = s[right]
        freq_map[right_char] = freq_map.get(right_char, 0) + 1
        max_freq = max(max_freq, freq_map[right_char])
        
        if (right - left + 1) - max_freq > k:
            # need to shrink
            left_char = s[left]
            freq_map[left_char] -= 1
            if freq_map[left_char] == 0:
                del freq_map[left_char]
            left += 1
        
        # calc
        max_length = max(max_length, right - left + 1)
        
    return max_length

print(func(s, k))

"""
Better approach:
- sliding window
- length of window - max freq character

optimal:
- only move the left pointer if needed (length - max freq) > k, but we use an if statement not while
- this works because we only want to find anything greater than our current max, which can never shrink below the current window we found

Problem Statement: Given an integer k and a string s, any character in the string can be selected and changed to any other uppercase English character. This operation can be performed up to k times. After completing these steps, return the length of the longest substring that contains the same letter.

Input: s = "BAABAABBBAAA", k = 2  
Output: 6  
Explanation: We can change the B at index 0 and 3 (0-based indexing) to A. The new string becomes "AAAAAABBBAAA". The substring "AAAAAA" is the longest substring with the same letter, and its length is 6. 


Input: s = "AABABBA", k = 1  
Output: 4  
Explanation: We can change one character to get the new string "AABBBBA". The substring "BBBB" is the longest with the same character. There are other ways to achieve this result as well.
"""
