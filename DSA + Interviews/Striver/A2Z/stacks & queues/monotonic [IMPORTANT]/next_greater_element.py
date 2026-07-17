arr = [6, 8, 0, 1, 3]

# stack = [4, 3]
# ans = [-1, 4, 4, 3]

# first pop any numbers less than the current number in the stack, then use any remaining to add to ans and -1 if there is no stack
    
def func(arr):
    stack = []
    ans = [0] * len(arr)
    
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        
        while stack and stack[-1] <= num:
            stack.pop()
            
        if stack:
            ans[i] = stack[-1]
        else:
            ans[i] = -1
            
        stack.append(num)
            
    return ans

print(func(arr))

"""
Problem Statement: Given an integer array A, return the next greater element for every element in A. The next greater element for an element x is the first element greater than x that we come across while traversing the array in a clockwise manner. If it doesn't exist, return -1 for this element.

Input: arr = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation: In the array, the next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4 is -1, since it does not exist.

Input : arr = [6, 8, 0, 1, 3]
Output: [8, -1, 1, 3, -1]
Explanation : In the array, the next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1 , for 1 it is 3 and then for 3 there is no larger element on the right and hence -1.
"""
