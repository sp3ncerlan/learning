height = [4,2,0,3,2,5]

# [4, 8, 5, 2, 25]
# stack = [2
    
def func(height):
    water = 0
    
    leftMax, rightMax = height[0], height[len(height) - 1]
    left, right = 1, len(height) - 1
    
    while left <= right:
        if height[left] <= height[right]:
            leftMax = max(leftMax, height[left])
            water += leftMax - height[left]
            left += 1
        else:
            rightMax = max(rightMax, height[right])
            water += rightMax - height[right]
            right -= 1
        
    return water

print(func(height))

"""
Problem Statement: Given an array of non-negative integers representation elevation of ground. Your task is to find the water that can be trapped after rain.

Input : height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output : 6
Explanation : Water is trapped in the dips between bars. The total trapped water units add up to 6 (1+1+2+1+1).

Input : height = [4,2,0,3,2,5]
Output : 9
Explanation : The elevation map traps 9 units of water in total, as water fills the spaces between higher bars on both sides.
"""
