"""
Problem Statement: You are given a positive integer n. Your task is to find and return its square root. If 'n' is not a perfect square, then return the floor value of sqrt(n).

Input: N = 36
Output: 6
Explanation: Square root of 36 is 6.

Input: N = 28
Output: 5
Explanation: Square root of 28 is approximately 5.292. So, the floor value will be 5. 
"""
num = 28

def search(num):
    left, right = 1, num // 2
    
    answer = -1
    while left <= right:
        sqrt = (left + right) // 2
        result = sqrt * sqrt
        
        if result <= num:
            answer = sqrt
            left = sqrt + 1
        else:
            right = sqrt - 1
            
    return answer

print(search(num))
