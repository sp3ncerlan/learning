import heapq

nums = [6, 5, 3, 2, 8, 10, 9]
k = 3

def func(nums, k):
    # fill
    min_heap = []
    for i in range(k + 1):
        heapq.heappush(min_heap, nums[i])
        
    ans = []
    
    for i in range(k + 1, len(nums)):
        ans.append(heapq.heappop(min_heap))
        heapq.heappush(min_heap, nums[i])
        
    while min_heap:
        ans.append(heapq.heappop(min_heap))
        
    return ans

print(func(nums, k))

"""
Problem Statement: Given an array nums, return the kth largest element in the array.
"""
