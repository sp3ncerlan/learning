n = 3

def recurse(n, op, cl, path, result):
    if op == n and cl == n:
        result.append(path)
        return
    
    if op < n:
        recurse(n, op + 1, cl, path + "(", result)
        
    if cl < op:
        recurse(n, op, cl + 1, path + ")", result)

def func(n):
    result = []
    
    recurse(n, 0, 0, "", result)
    
    return result

print(func(n))

"""
Problem Statement: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input:
 n = 3
Output:
 ["((()))", "(()())", "(())()", "()(())", "()()()"]

Example 2:
Input:
 n = 1
Output:
 ["()"]
"""
