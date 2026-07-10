x = 2
n = -1

def recurse(x, n):
    if n == 0:
        return 1.0
    
    if n == 1:
        return x

    # if even, divide n by 2 and multiply x by 2    
    if n % 2 == 0:
        return recurse(x * x, n / 2.0)
    else:
        return x * recurse(x, n - 1)

def func(x, n):
    if n < 0:
        return 1.0 / recurse(x, -n)
        
    return recurse(x, n)

print(func(x, n))

"""
Problem Statement: Implement the power function pow(x, n) , which calculates the x raised to n i.e. xn.

Example 1:
Input:
 x = 2.0000, n = 10  
Output:
 1024.0000  
Explanation:
 The answer is calculated as 2^10, which equals 1024.

Example 2:
Input:
 x = 2.0000, n = -2  
Output:
 0.2500  
Explanation:
 The answer is calculated as 2^(-2), which is equal to 1/4 = 0.25.
"""
