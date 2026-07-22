heights = [2, 1, 5, 6, 2, 3]
N = 6

def func(heights, N):
    n = len(heights)
    stack = []
    largest = 0
    
    for i in range(n + 1):
        current_height = heights[i] if i < n else 0
        
        while stack and (i == n or heights[stack[-1]] >= current_height):
            height = heights[stack.pop()]
            
            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1
            
            largest = max(largest, height * width)
            
        stack.append(i)
            
    return largest

print(func(heights, N))

"""
- monotonically increasing stack
- while the current number is smaller than the top of the stack
    - we pop the top, then compare with the next top of the stack to calc max rectangle at this moment
"""
