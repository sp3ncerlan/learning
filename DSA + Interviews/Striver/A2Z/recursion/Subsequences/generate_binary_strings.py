n = 3

def recurse(n, curr, result):
    if len(curr) == n:
        result.append(curr)
        return
    
    recurse(n, curr + "0", result)
    
    if not curr or curr[-1] != '1':
        recurse(n, curr + "1", result)

def func(n):
    result = []
    
    recurse(n, "", result)
    
    return result

print(func(n))

"""
Problem Statement: Given an integer n, return all binary strings of length n that do not contain consecutive 1s. Return the result in lexicographically increasing order.

A binary string is a string consisting only of characters '0' and '1'.

Example 1:
Input:
 n = 3  
Output:
 ["000", "001", "010", "100", "101"]  
Explanation:
 All binary strings of length 3 that do not contain consecutive 1s.

Example 2:
Input:
 n = 2  
Output:
 ["00", "01", "10"]  
Explanation:
 All binary strings of length 2 that do not contain consecutive 1s.
"""
