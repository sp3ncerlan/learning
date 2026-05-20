"""
Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

The union of two arrays can be defined as the common and distinct elements in the two arrays.

NOTE: Elements in the union should be in ascending order.

BRUTE FORCE:
- check for each number in a set and add it to the set if not seen before
- O((n + m) log(n + m))

OPTIMAL:
- we want to sort at the same time as iterating
- start a pointer at each arr, compare and increment whichever one
- check if the last element we inserted is equal to the current, if so then we increment
- if the elements are the same then we compare/insert once and increment both
"""

n, m = 10, 7
arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [2,3,4,4,5,11,12]

def func(arr1, arr2, n, m):
    ptr1, ptr2 = 0, 0
    
    result = []
    while ptr1 < n and ptr2 < m:
        if arr1[ptr1] == arr2[ptr2]:
            if not result or result[-1] != arr1[ptr1]:
                result.append(arr1[ptr1])
            ptr1 += 1
            ptr2 += 1
        elif arr1[ptr1] < arr2[ptr2]:
            if not result or result[-1] != arr1[ptr1]:
                result.append(arr1[ptr1])
            ptr1 += 1
        else:
            if not result or result[-1] != arr2[ptr2]:
                result.append(arr2[ptr2])
            ptr2 += 1
            
    while ptr1 < n:
        if not result or result[-1] != arr1[ptr1]:
            result.append(arr1[ptr1])
        ptr1 += 1
    
    while ptr2 < m:
        if not result or result[-1] != arr2[ptr2]:
            result.append(arr2[ptr2])
        ptr2 += 1
    
    return result

print(func(arr1, arr2, n, m))
