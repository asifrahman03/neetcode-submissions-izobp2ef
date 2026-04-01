class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            val1 = -heapq.heappop(max_heap)
            val2 = -heapq.heappop(max_heap)
            res = val1 - val2
            if res == 0 and len(max_heap) == 0:
                heapq.heappush(max_heap, -res)
            else:
                heapq.heappush(max_heap, -res)
        return -max_heap[0]

