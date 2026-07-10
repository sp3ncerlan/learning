stack = [4, 1, 3, 2]

def insert_at_bottom(stack, val):
    if not stack:
        stack.append(val)
        return
    
    top_val = stack.pop()
    insert_at_bottom(stack, val)
    stack.append(top_val)

def reverse_stack(stack):
    if not stack:
        return
    
    top_val = stack.pop()
    reverse_stack(stack) 
    
    insert_at_bottom(stack, top_val)

reverse_stack(stack)
print(stack)

"""
- recursion saves each value in place
- we can recursively pop, then once the stack is empty, we append so it will add everything in reverse

Problem Statement: You are given a stack of integers. Your task is to reverse the stack using recursion. You may only use standard stack operations (push, pop, top/peek, isEmpty). You are not allowed to use any loop constructs or additional data structures like arrays or queues.

Your solution must modify the input stack in-place to reverse the order of its elements.

Example 1:
Input:
 stack = [4, 1, 3, 2]  
Output:
 [2, 3, 1, 4]

Example 2:
Input:
 stack = [10, 20, -5, 7, 15]  
Output:
 [15, 7, -5, 20, 10]
"""
