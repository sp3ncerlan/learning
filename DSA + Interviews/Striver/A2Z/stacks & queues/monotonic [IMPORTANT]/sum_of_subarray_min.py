arr = [3, 1, 2, 5]

# stack = []

def findNSE(arr):
    n = len(arr)
    
    ans = [0] * n
    stack = []
    
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
            
        ans[i] = stack[-1] if stack else n
        
        stack.append(i)
        
    return ans

# [1, 2, 3, 2, 1]
# stack = [1, 3, 3]
    
def findPSEE(arr):
    n = len(arr)
    
    ans = [0] * n
    stack = []
    
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
            
        ans[i] = stack[-1] if stack else -1
        
        stack.append(i)
        
    return ans
    
def func(arr):
    nse = findNSE(arr)
    psee = findPSEE(arr)

    n = len(arr)
    
    mod = int(1e9 + 7)
    
    total = 0
    
    for i in range(n):
        left = i - psee[i]
        right = nse[i] - i
        
        freq = left * right * 1
        
        val = (freq * arr[i]) % mod
        
        total = (total + val) % mod
        
    return total

print(func(arr))

"""
Problem Statement: Given an array of integers arr of size n, calculate the sum of the minimum value in each (contiguous) subarray of arr. Since the result may be large, return the answer modulo 10⁹ +7.

Example 1:
Input:
 arr = [3, 1, 2, 5]
Output:
 18
Explanation:
 The minimum of subarrays: [3], [1], [2], [5], [3, 1], [1, 2], [2, 5], [3, 1, 2], [1, 2, 5], [3, 1, 2, 5] are 3, 1, 2, 5, 1, 1, 2, 1, 1, 1 respectively and their sum is 18.

Example 2:
Input:
 arr = [2, 3, 1]
Output:
 10
Explanation:
 The minimum of subarrays: [2], [3], [1], [2,3], [3,1], [2,3,1] are 2, 3, 1, 2, 1, 1 respectively and their sum is 10.
"""
