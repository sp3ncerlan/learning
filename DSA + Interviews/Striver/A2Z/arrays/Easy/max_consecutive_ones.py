"""
Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

Example 1:
Input: prices = {1, 1, 0, 1, 1, 1}
Output: 3
Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.

Example 2:
Input: prices = {1, 0, 1, 1, 0, 1} 
Output: 2
Explanation: There are two consecutive 1's in the array.         
"""

def max_consecutive_ones(arr) -> int:
    max_consec = 0
    current_consec = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            current_consec += 1
        else:
            current_consec = 0
        
        max_consec = max(max_consec, current_consec)
    
    return max_consec

arr = [1, 1, 0, 1, 1, 1]

print(max_consecutive_ones(arr))
