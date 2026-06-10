# def func(arr, k):
#     n = len(arr)
#     how_many = [0] * (n - 1)
    
#     for _ in range(k):
#         max_section = -1
#         max_ind = -1
        
#         for i in range(n - 1):
#             diff = arr[i + 1] - arr[i]
#             section_length = diff / (how_many[i] + 1)
#             if section_length > max_section:
#                 max_section = section_length
#                 max_ind = i
        
#         how_many[max_ind] += 1
        
#     max_ans = -1
#     for i in range(n - 1):
#         diff = arr[i + 1] - arr[i]
#         section_length = diff / (how_many[i] + 1)
#         if section_length > max_ans:
#             max_ans = section_length
    
#     return max_ans

# def gas_stations(arr, k):
#     # array to keep track of placed gas stations
#     # max-heap
#     n = len(arr)
#     how_many = [0] * (n - 1)
#     max_heap = [] # (section_length, index) -> arr[i + 1] - arr[i] / (how_many[i] + 1)
    
#     for i in range(n - 1):
#         diff = arr[i + 1] - arr[i]
#         heapq.heappush(max_heap, (-diff, i))
    
#     while k > 0:
#         _, index = heapq.heappop(max_heap)
#         diff = arr[index + 1] - arr[index]
        
#         how_many[index] += 1
#         section_length = diff / (how_many[index] + 1)
        
#         heapq.heappush(max_heap, (-section_length, index))
        
#         k -= 1
    
#     return -max_heap[0][0]

def gas_stations_possible(arr, dist):
    count = 0
    n = len(arr)
    
    for i in range(1, n):
        number_in_between = int((arr[i] - arr[i - 1]) / dist)
        
        if (arr[i] - arr[i - 1]) == dist * number_in_between:
            number_in_between -= 1
        
        count += number_in_between

    return count
    
def func(arr, k):
    n = len(arr)
    
    max_dist = 0
    for i in range(n - 1):
        dist = arr[i + 1] - arr[i]
        max_dist = max(max_dist, dist)
    
    left, right = 0, float(max_dist)
    
    optimal = -1
    while (right - left) > 10**-6:
        dist = (left + right) / 2.0
        
        if gas_stations_possible(arr, dist) > k:
            optimal = dist
            left = dist
        else:
            right = dist
    
    return optimal

import heapq

arr = [1,2,3,4,5]
k = 4
        
print(func(arr, k))

"""
Problem Statement: You are given a sorted array 'arr' of length 'n', which contains positive integer positions of 'n' gas stations on the X-axis. You are also given an integer 'k'. You have to place 'k' new gas stations on the X-axis. You can place them anywhere on the non-negative side of the X-axis, even on non-integer positions. Let 'dist' be the maximum value of the distance between adjacent gas stations after adding k new gas stations. Find the minimum value of 'dist'.

Example 1:
Input Format: N = 5, arr[] = {1,2,3,4,5}, k = 4
Result: 0.5
Explanation: One of the possible ways to place 4 gas stations is {1,1.5,2,2.5,3,3.5,4,4.5,5}. Thus the maximum difference between adjacent gas stations is 0.5. Hence, the value of 'dist' is 0.5. It can be shown that there is no possible way to add 4 gas stations in such a way that the value of 'dist' is lower than this. 

Example 2:
Input Format: N = 10, arr[] = {1,2,3,4,5,6,7,8,9,10}, k = 1
Result: 1
Explanation: One of the possible ways to place 1 gas station is {1,1.5,2,3,4,5,6,7,8,9,10}. Thus the maximum difference between adjacent gas stations is still 1. Hence, the value of 'dist' is 1. It can be shown that there is no possible way to add 1 gas station in such a way that the value of 'dist' is lower than this.

- we're trying to distribute gas stations so that we minimize the distance between any two of them. for this, we want to basically evenly split the space between each index so that we don't have any adjacent value that is greater than the limit we create
            
BF:
- we start with 0.1, then keep going up and see if the amount of stations we placed is at least equal to k or more. if so, we increase the space and try again

OPTIMAL:
- binary search as well, but our while loop condition is while (high - low > 10^(-6)), since we are dealing with floating point and theoretically it could divide infinitely and never cross
"""
