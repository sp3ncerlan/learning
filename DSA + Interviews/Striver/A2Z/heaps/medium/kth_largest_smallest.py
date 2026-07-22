import heapq

nums = [1, 2, 3, 4, 5]
k = 2

def func(nums, k):
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    return min_heap[0]

print(func(nums, k))

"""
Problem Statement: Given an array nums, return the kth largest element in the array.
"""
