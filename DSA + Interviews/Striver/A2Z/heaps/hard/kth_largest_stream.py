import heapq
class Solution:

    # Constructor initializes the heap with k largest elements
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums[:]
        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    # Adds new value and returns the k-th largest
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]

# Driver code
nums = [4, 5, 8, 2]
kthLargest = Solution(3, nums)
print(kthLargest.add(3))   # Output: 4
print(kthLargest.add(5))   # Output: 5
print(kthLargest.add(10))  # Output: 5
print(kthLargest.add(9))   # Output: 8
print(kthLargest.add(4))   # Output: 8
