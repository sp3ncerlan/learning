heights = [2, 1, 5, 6, 2, 3]
N = 6

"""
- find both PSEE and NSE to see how far left and right current index height can go, then calculate the max area
"""

# def findNSE(heights):
#     n = len(heights)
    
#     stack = []
#     ans = [0] * n
    
#     for i in range(n - 1, -1, -1):
#         while stack and heights[stack[-1]] >= heights[i]:
#             stack.pop()
            
#         ans[i] = stack[-1] if stack else n
        
#         stack.append(i)
        
#     return ans
    
# def findPSEE(heights):
#     n = len(heights)
    
#     stack = []
#     ans = [0] * n
    
#     for i in range(n):
#         while stack and heights[stack[-1]] > heights[i]:
#             stack.pop()
            
#         ans[i] = stack[-1] if stack else -1
        
#         stack.append(i)
        
#     return ans

# 2, 1, 5, 6, 2, 3
"""
stack = [1]
height = 5

width = 4 - 1 - 1 = 2
"""
    
def func(N, heights):
    n = len(heights)
    
    max_area = 0
    stack = []
    
    for i in range(n):
        current_height = heights[i] if i < n else 0
        
        while stack and heights[stack[-1]] >= current_height:
            height = heights[stack.pop()]
            
            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1
            
            max_area = max(max_area, height * width)
        
        stack.append(i)
        
    return max_area

print(func(N, heights))

"""
Problem Statement: Given an array of integers heights representing the histogram's bar height where the width of each bar is 1 return the area of the largest rectangle in histogram.

Example:
Input: N =6, heights[] = {2,1,5,6,2,3}
Output: 10
"""
