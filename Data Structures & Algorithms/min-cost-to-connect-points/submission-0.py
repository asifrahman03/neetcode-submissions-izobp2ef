class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        def calcDistance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2

            res = abs(x1-x2) + abs(y1 - y2)
            return res

        min_heap = [(0, 0)]
        visited = set()
        res = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = calcDistance(points[i], points[j])
                adj[i].append((distance, j))
                adj[j].append((distance, i))
            
        while len(visited) < len(points):
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            for c, n in adj[node]:
                if n not in visited:
                    heapq.heappush(min_heap, (c, n))
        return res