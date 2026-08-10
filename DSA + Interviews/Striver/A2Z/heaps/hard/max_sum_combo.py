import heapq

nums1 = [7, 3]
nums2 = [1, 6]
k = 2

"""
- we have to use one from each list
    - we can reuse numbers

BF:
- get all sums and add to heap of size k

Optimal:
- keep a set and do a BFS
- (sum, index1, index2)
- heap gets max sum
- reinsert if not seen index combo before
"""

def func(nums1, nums2, k):
    max_heap = []

    nums1.sort(reverse=True)
    nums2.sort(reverse=True)

    heapq.heappush(max_heap, (-(nums1[0] + nums2[0]), 0, 0))
    visited = {(0, 0)}

    ans = []
    for _ in range(k):
        if not max_heap:
            break

        current_sum, index1, index2 = heapq.heappop(max_heap)
        current_sum = -current_sum

        if index1 + 1 < len(nums1):
            new_index1 = index1 + 1
            if (new_index1, index2) not in visited:
                visited.add((new_index1, index2))
                heapq.heappush(max_heap, (-(nums1[new_index1] + nums2[index2]), new_index1, index2))

        if index2 + 1 < len(nums2):
            new_index2 = index2 + 1
            if (index1, new_index2) not in visited:
                visited.add((index1, new_index2))
                heapq.heappush(max_heap, (-(nums1[index1] + nums2[new_index2]), index1, new_index2))

        ans.append(current_sum)

    return ans

print(func(nums1, nums2, k))