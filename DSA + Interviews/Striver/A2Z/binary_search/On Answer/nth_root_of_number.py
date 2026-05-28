"""
Problem Statement: Given two numbers N and M, find the Nth root of M. The nth root of a number M is defined as a number X when raised to the power N equals M. If the 'nth root is not an integer, return -1.

Input: N = 3, M = 27
Output: 3
Explanation: The cube root of 27 is equal to 3.

Input : N = 4, M = 69
Output: -1
Explanation : The 4th root of 69 does not exist. So, the answer is -1.
"""
N, M = 4, 69

def search(N, M):
    # what is the range
    left, right = 1, M**0.5
    
    ans = -1
    while left <= right:
        current = (left + right) // 2
        calc = current**N
        
        if calc == M:
            ans = int(current)
            break
        elif calc > M:
            right = current - 1
        else:
            left = current + 1
    
    return ans

print(search(N, M))
