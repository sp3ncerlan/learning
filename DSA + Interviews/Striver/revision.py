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
arr = [3, 2, 1, 4]
# k = 4

def merge(arr, low, mid, high):
    temp = []
    
    left, right = low, mid + 1
    
    while left <= mid and right <= high:
        # compare and merge while counting inverted pairs
        if arr[left] > arr[right]:
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

def countPairs(arr, low, mid, high):
    pairs = 0
    
    left = low
    for right in range(mid + 1, high + 1):
        while left <= mid and arr[left] <= 2 * arr[right]:
            left += 1
        pairs += (mid - left + 1)
    
    return pairs

def mergeSort(arr, low, high):
    reverse_pairs = 0
    
    if low >= high:
        return reverse_pairs
    
    mid = (low + high) // 2
    
    reverse_pairs += mergeSort(arr, low, mid)
    reverse_pairs += mergeSort(arr, mid + 1, high)
    reverse_pairs += countPairs(arr, low, mid, high)
    
    merge(arr, low, mid, high)
    
    return reverse_pairs

print(mergeSort(arr, 0, len(arr) - 1))

"""
OPTIMAL:
- we cannot do the comparison step in the merge step because we are comparing different things
- we will first compare the values, then merge them
"""
