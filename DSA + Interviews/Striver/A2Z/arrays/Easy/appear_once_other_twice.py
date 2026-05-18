"""
Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

Example 1:
Input Format: arr[] = {2,2,1}
Result: 1
Explanation: In this array, only the element 1 appear once and so it is the answer.


Example 2:
Input Format: arr[] = {4,1,2,1,2}
Result: 4
Explanation: In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.       
"""

def appear_once_other_twice(arr) -> int:
    single = 0
    
    for num in arr:
        single ^= num
    
    return single

arr = [4,1,2,1,2]

print(appear_once_other_twice(arr))
