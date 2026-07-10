str = "abc"

def recurse(str, start, path, result):
    if path:
        result.append("".join(path))
        
    for i in range(start, len(str)):
        path.append(str[i])
        recurse(str, i + 1, path, result)
        path.pop()
    
def func(str):
    result = []
    recurse(str, 0, [], result)
    return result

print(func(str))

"""
Problem Description: Given a string, find all the possible subsequences of the string.

Input: str = "abc"
Output: [a, ab, abc, ac, b, bc, c]
Explanation: Given string has 7 subsequences.
Input: str = "aa"
Output: [a, a, aa] 
Explanation: Given string has 3 subsequences.
"""
