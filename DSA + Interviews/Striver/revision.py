from itertools import permutations
from collections import defaultdict
import math
import bisect

# matrix = [[1, 4, 9], [2, 5, 6], [3, 8, 7]]
# arr1 = [1, 2]
# arr2 = [3, 4]
# k =
s = " -12345"
# t = "bar"
# arr = [1, 2, 3, 4, 5]
# k = 4
x = 2.0000
n = 10
# MOD = 10**9 + 7

def helper(x, n):
    if n == 0:
        return 1.0
    
    if n == 1:
        return x
    
    result = 0
    if n % 2 == 0:
        result = (result + helper(x * x, n // 2))
    else:
        result = (result + (x * helper(x, n - 1)))
    
    return result

def func(x, n):
    if n < 0:
        return 1.0 / helper(x, -n)

    return helper(x, n)
    
print(func(x, n))

"""
OPTIMAL:
- if we just multiplied the numbers one by one, it would be o(n)
- we can do it faster in o(logn)
    - every time the power is even, we can divide it in half and then make the base number multiplied
    - if its odd, we want to make it even, so we just subtract one and multiply the result
"""
