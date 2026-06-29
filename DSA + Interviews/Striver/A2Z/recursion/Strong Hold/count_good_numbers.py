n = 1

MOD = 10**9 + 7

def func(index, n):
    if index == n:
        return 1
    
    result = 0
    
    # even
    if index % 2 == 0:
        even_digits = [0, 2, 4, 6, 8]
        for digit in even_digits:
            result += func(index + 1, n) % MOD
    else:
        prime_digits = [2, 3, 5, 7]
        for digit in prime_digits:
            result += func(index + 1, n) % MOD
            
    return result

print(func(0, n))

"""
Problem Statement: A digit string is considered good if the digits at even indices (0-based) are even digits (0, 2, 4, 6, 8) and the digits at odd indices are prime digits (2, 3, 5, 7).

Given an integer n, return the total number of good digit strings of length n. As the result may be large, return it modulo 109 + 7.

A digit string is a string consisting only of the digits '0' through '9'. It may contain leading zeros.

Example 1:
Input:
 n = 1
Output:
 5
Explanation:
 Only one index (0) → must be even.
Valid strings: "0", "2", "4", "6", "8"

Example 2:
Input:
 n = 2
Output:
 20
Explanation:
 Index 0: 5 options (even digits)
Index 1: 4 options (prime digits)
Total: 5 * 4 = 20
"""
