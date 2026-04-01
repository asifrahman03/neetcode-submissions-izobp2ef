class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for source, target, value in times:
            adj_list[source].append((target, value))
        
        visited = set()
        min_heap = [(0, k)]
        # dist = [float('inf') for k in range(n+1)]
        # dist[k] = 0
        res = 0
        while min_heap:
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            res = cost
            for nei, time in adj_list[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (cost + time, nei))
        return res if len(visited) == n else -1

        # q = deque([(k, 0)])
        # res = 0
        # while q:
        #     node, cost = q.popleft()
        #     if len(visited) == n:
        #         return res
        #     res += cost
        #     for nei, time in adj_list[node]:
        #         if nei not in visited:
        #             visited.add(nei)
        #             q.append((nei, time))
        # return -1

        