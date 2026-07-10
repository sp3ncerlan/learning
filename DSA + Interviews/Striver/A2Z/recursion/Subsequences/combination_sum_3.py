k = 3
n = 7

def recurse(k, n, result, path, total, count, last):
    if count == k:
        if total == n:
            result.append(path[:])
        return
    
    for num in range(last, 10):
        path.append(num)
        recurse(k, n, result, path, total + num, count + 1, num + 1)
        path.pop()
    
def func(k, n):
    result = []
    path = []
    
    recurse(k, n, result, path, 0, 0, 1)
    
    return result

print(func(k, n))

"""
Problem Statement: Determine all possible set of k numbers that can be added together to equal n while meeting the following requirements:
1. There is only use of numerals 1 through 9.
2. A single use is made of each number.
Return list of every feasible combination that is allowed. The combinations can be returned in any order, but the list cannot have the same combination twice.

Example 1:
Input:
 k = 3, n = 7
Output:
 [[1, 2, 4]]
Explanation:

1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input:
 k = 3, n = 9
Output:
 [[1, 2, 6],[1, 3, 5],[2, 3, 4]]
Explanation:

1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
"""
