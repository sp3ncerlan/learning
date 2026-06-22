from itertools import permutations
from collections import defaultdict
import math
import bisect

# matrix = [[1, 4, 9], [2, 5, 6], [3, 8, 7]]
# arr1 = [1, 2]
# arr2 = [3, 4]
# k =
# s = " amazing coding skills "
# t = "bar"
arr = [5, 4, 3, 2, 1]
# k = 4

def merge(arr, low, mid, high):
    inversions = 0
    temp = []
    
    left, right = low, mid + 1
    
    while left <= mid and right <= high:
        # compare and merge while counting inverted pairs
        if arr[left] > arr[right]:
            inversions += (mid - left + 1)
            temp.append(arr[right])
            right += 1
        else:
            temp.append(arr[left])
            left += 1
    
    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]
        
    return inversions

def mergeSort(arr, low, high):
    inversions = 0
    
    if low >= high:
        return inversions
    
    mid = (low + high) // 2
    
    inversions += mergeSort(arr, low, mid)
    inversions += mergeSort(arr, mid + 1, high)
    inversions += merge(arr, low, mid, high)
    
    return inversions

print(mergeSort(arr, 0, len(arr) - 1))

"""
BF:
"""
