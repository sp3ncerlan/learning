arr = [3, 5, 1]
k = 3

def calc_splits(arr, count):
    groups = 1
    
    current_group = 0
    for num in arr:
        if current_group + num > count:
            groups += 1
            current_group = num
        else:
            current_group += num
        
    return groups

def func(arr, k):
    left, right = max(arr), sum(arr)
    
    optimal = -1
    while left <= right:
        count = (left + right) // 2
        
        if calc_splits(arr, count) <= k:
            optimal = count
            right = count - 1
        else:
            left = count + 1
            
    return optimal
        
print(func(arr, k))

"""
Problem Statement: Given an integer array 'A' of size 'N' and an integer 'K'. Split the array 'A' into 'K' non-empty subarrays such that the largest sum of any subarray is minimized. Your task is to return the minimized largest sum of the split. A subarray is a contiguous part of the array.

Example 1:
Input Format: N = 5, a[] = {1,2,3,4,5}, k = 3
Result: 6
Explanation: There are many ways to split the array a[] into k consecutive subarrays. The best way to do this is to split the array a[] into [1, 2, 3], [4], and [5], where the largest sum among the three subarrays is only 6.

Example 2:
Input Format: N = 3, a[] = {3,5,1}, k = 3
Result: 5
Explanation: There is only one way to split the array a[] into 3 subarrays, i.e., [3], [5], and [1]. The largest sum among these subarrays is 5.

BF:
- helper method to check how many split groups we can make
- main method for loop that checks each split group counts from min(arr) to sum(arr)
    - min(arr) allows for 5 split groups, sum(arr) allows for 1 split group, two extremes

OPTIMAL:
"""
