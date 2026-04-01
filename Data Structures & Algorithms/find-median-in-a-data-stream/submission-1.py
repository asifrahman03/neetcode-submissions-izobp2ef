class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if self.min_heap and num  > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        if abs(len(self.min_heap) - len(self.max_heap)) > 1:
            if len(self.min_heap) > len(self.max_heap):
                val = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -val)
            else:
                val = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, val)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            res = (self.min_heap[0] + -self.max_heap[0]) / 2
        elif len(self.min_heap) > len(self.max_heap):
            res = self.min_heap[0]
        else:
            res = -self.max_heap[0]
        return res

        
        