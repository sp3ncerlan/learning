from itertools import permutations
import math

arr = [4, 2, 1, 3, 6]
k = 2

def can_fit(arr, k, distance):
    count = 1
    lastPos = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] - lastPos >= distance:
            count += 1
            lastPos = arr[i]
        
        if count >= k:
            return True

    return False

def func(arr, k):
    arr.sort()
    
    left, right = 1, arr[-1] - arr[0]
    
    result = 0
    while left <= right:
        distance = (left + right) // 2
        
        if can_fit(arr, k, distance):
            result = distance
            left = distance + 1
        else:
            right = distance - 1
    
    return result
        
print(func(arr, k))

"""
Problem Statement: You are given an array 'arr' of size 'n' which denotes the position of stalls. You are also given an integer 'k' which denotes the number of aggressive cows.
You are given the task of assigning stalls to 'k' cows such that the minimum distance between any two of them is the maximum possible. Find the maximum possible minimum distance.

Example 1:
Input Format:
 N = 6, k = 4, arr[] = {0,3,4,7,10,9}
Result:
 3
Explanation:
 The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions {0, 3, 7, 10}. Here the distances between cows are 3, 4, and 3 respectively. We cannot make the minimum distance greater than 3 in any ways.

Example 2:
Input Format:
 N = 5, k = 2, arr[] = {4,2,1,3,6}
Result:
 5
Explanation:
 The maximum possible minimum distance between any two cows will be 5 when 2 cows are placed at positions {1, 6}. 

BF:
- try each possible distance and see if we can fit all cows with that distance
- if we can't at any point, return the previous distance since thats the one that worked
- o(nlogn) + o(n * max(arr) - min(arr)), o(1)

OPTIMAL:
- binary search
- search space is the distance we try between cows, so left is 1 and right is the max distance possible (maximum stall - minimum stall)
- o(nlogn) + o(n * log(max(arr) - min(arr))), o(1)
"""
