asteroids = [-20, -10, -2]
    
def func(asteroids):
    stack = []
    
    for a in asteroids:
        if a > 0:
            stack.append(a)
        else:
            while stack and stack[-1] > 0 and stack[-1] < abs(a):
                stack.pop()
                
            if not stack or stack[-1] < 0:
                stack.append(a)
            elif stack[-1] == abs(a):
                stack.pop()
                
    return stack

print(func(asteroids))

"""
Problem Statement: Given an array of integers asteroids, where each integer represents an asteroid in a row, determine the state of the asteroids after all collisions. In this array, the absolute value represents the size of the asteroid, and the sign represents its direction (positive meaning right and negative meaning left). All asteroids move at the same speed.

When two asteroids meet, the smaller one will explode. If they are the same size, both will explode. Asteroids moving in the same direction will never meet.

Example 1:
Input:
 asteroids = [2, -2]
Output:
 []
Explanation:
 The asteroid with size 2 and the one with size -2 collide, exploding each other.

Example 2:
Input:
 asteroids = [10, 20, -10]
Output:
 [10, 20]
Explanation:
 The asteroid with size 20 and the one with size -10 collide, resulting in the remaining asteroid with size 20. The asteroids with sizes 10 and 20 never collide.
"""
