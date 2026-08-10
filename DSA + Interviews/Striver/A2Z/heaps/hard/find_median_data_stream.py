import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = [] # left side
        self.min_heap = [] # right side

    # Function to add a number to the data stream
    def addNum(self, num):
        heapq.heappush(self.min_heap, num)
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        print(self.min_heap, self.max_heap)

        # left side will always have the higher value in odd cases
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    # Function to find the median
    def findMedian(self):
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -self.max_heap[0]) / 2.0
        else:
            return self.min_heap[0]

# Driver code
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())  # 1.5
mf.addNum(3)
print(mf.findMedian())  # 2
