from itertools import permutations
from collections import defaultdict
import math

# matrix = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
# arr1 = [1, 2]
# arr2 = [3, 4]
# k =
s = "aabcbaa"
# t = "bar"
# arr = [1, 1, 3, 5, 5]
# k = 3

def func(s):
    result = 0
    
    for i in range(len(s)):
        freq = [0] * 26
        
        for j in range(i, len(s)):
            freq[ord(s[j]) - ord('a')] += 1
        
            maximum = max(freq)
            minimum = min(val for val in freq if val > 0)
            result += (maximum - minimum)
        
    return result

print(func(s))

"""
BF:
"""
