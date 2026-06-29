stack = [4, 1, 3, 2]

def insert(stack, temp):
    if not stack or stack[-1] >= temp:
        stack.append(temp)
        return
    
    val = stack.pop()
    insert(stack, temp)
    stack.append(val)

def sortStack(stack):
    if stack:
        temp = stack.pop()
        sortStack(stack)
        insert(stack, temp)
        
    return stack

print(sortStack(stack))

"""
Problem Statement: You are given a stack of integers. Your task is to sort the stack in descending order using recursion, such that the top of the stack contains the greatest element. You are not allowed to use any loop-based sorting methods (e.g., quicksort, mergesort). You may only use recursive operations and the standard stack operations (push, pop, peek/top, and isEmpty).

Example 1:
Input:
 stack = [4, 1, 3, 2]
Output:
 [4, 3, 2, 1]
Explanation:
 After sorting, the largest element (4) is at the top, and the smallest (1) is at the bottom.

Example 2:
Input:
 stack = [1]
Output:
 [1]
Explanation:
 A single-element stack is already sorted.
"""
