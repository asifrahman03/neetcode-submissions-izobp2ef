class MedianFinder:

    def __init__(self):
        self.min_h = []
        self.max_h = []

    def addNum(self, num: int) -> None:
        if len(self.min_h) == 0 or self.min_h[0] < num:
            heapq.heappush(self.min_h, num)
        else:
            heapq.heappush(self.max_h, -num)
            
        if abs(len(self.min_h) - len(self.max_h)) >= 2:
            if len(self.max_h) > len(self.min_h):
                while abs(len(self.min_h) - len(self.max_h)) >= 2:
                    val = heapq.heappop(self.max_h)
                    heapq.heappush(self.min_h, -val)
            else:
                while abs(len(self.min_h) - len(self.max_h)) >= 2:
                    val = heapq.heappop(self.min_h)
                    heapq.heappush(self.max_h, -val)
        

    def findMedian(self) -> float:
        if len(self.min_h) > len(self.max_h):
            return self.min_h[0]
        elif len(self.min_h) < len(self.max_h):
            return -self.max_h[0]
        else:
            return (self.min_h[0] + -self.max_h[0]) / 2
        