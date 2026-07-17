"""
Problem Statement: Given an array of integers arr, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Input: arr = [4,0,-1,3,5,3,6,8], k = 3
Output: [4,3,5,5,6,8]
Explanation: 

Window position                   Max
------------------------         -----
[4  0  -1] 3  5  3  6  8           4
 4 [0  -1  3] 5  3  6  8           3
 4  0 [-1  3  5] 3  6  8           5
 4  0  -1 [3  5  3] 6  8           5
 4  0  -1  3 [5  3  6] 8           6
 4  0  -1  3  5 [3  6  8]          8

For each window of size k=3, we find the maximum element in the window and add it to our output array.

Input: arr= [20,25], k = 2
Output: [25]
Explanation: There's just one window is size 2 that is possible and the maximum of the two elements is our answer.

create a queue
- queue keeps track of the maximum (always needs to be at the top)
    - in order to do this, we can push indices and query them to get the value
- each time we get the maximum and append to result, we check two things
    1. pop all the values that are lower than the current value we look at
    2. the front and whether it is out of bounds (current index - k)
"""

from collections import deque

arr = [4,0,-1,3,5,3,6,8]
k = 3

def func(arr, k):
    queue = deque()
    ans = []
    
    left = 0
    for right in range(len(arr)):       
        # check first index
        if queue and queue[0] < left:
            queue.popleft()
            
        while queue and arr[queue[-1]] < arr[right]:
            queue.pop()
            
        queue.append(right)
            
        if right - left + 1 == k:
            ans.append(arr[queue[0]])
            left += 1
            
    return ans

print(func(arr, k))
