arr = [4, 8, 5, 2, 25]

# [4, 8, 5, 2, 25]
# stack = [2
    
def func(arr):
    stack = []
    ans = [-1] * len(arr)
    
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        
        while stack and stack[-1] >= arr[i]:
            stack.pop()
            
        if stack:
            ans[i] = stack[-1]
            
        stack.append(num)
        
    return ans

print(func(arr))

"""
Problem Statement: Given an array of integers arr, your task is to find the Next Smaller Element (NSE) for every element in the array.
The Next Smaller Element for an element x is defined as the first element to the right of x that is smaller than x.
If there is no smaller element to the right, then the NSE is -1.

Example 1:
Input:
 arr = [4, 8, 5, 2, 25]
Output:
 [2, 5, 2, -1, -1]
Explanation:

- For 4, the next smaller element is 2.
- For 8, the next smaller element is 5.
- For 5, the next smaller element is 2.
- For 2, there is no smaller element to its right → -1.
- For 25, no smaller element exists → -1.

Example 2:
Input:
 arr = [10, 9, 8, 7]
Output:
 [9, 8, 7, -1]
Explanation:

Each element's next right neighbor is smaller.
Each element's next right neighbor is smaller.
"""
