class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        m_heap = []


        for point in points:
            x, y = point
            distance = math.sqrt((x**2) + (y**2))
            if len(m_heap) < k:
                heapq.heappush(m_heap, [-distance, point])
                continue
            while len(m_heap) > k:
                heapq.heappop(m_heap)
            if -m_heap[0][0] > distance:
                heapq.heappop(m_heap)
                heapq.heappush(m_heap, [-distance, point])
        for p in m_heap:
            _, point = p
            res.append(point)
        return res