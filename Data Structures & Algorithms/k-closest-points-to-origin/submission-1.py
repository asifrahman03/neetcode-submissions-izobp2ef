class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_h = []
        res = []

        for i, point in enumerate(points):
            x, y = point
            distance = math.sqrt( ((0 - x)**2) + ((0 - y)**2) )
            if len(max_h) < k:
                heapq.heappush(max_h, (-distance, i))
                continue
            if distance < -max_h[0][0]:
                heapq.heappop(max_h)
                heapq.heappush(max_h, (-distance, i))
        for pair in max_h:
            index = pair[1]
            res.append(points[index])
        return res
        
