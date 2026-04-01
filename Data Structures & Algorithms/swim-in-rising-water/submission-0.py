class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        distance = [[float('inf') for i in range(len(grid))] for j in range(len(grid))]
        distance[0][0] = grid[0][0]
        ROWS = len(grid)
        COLS = len(grid[0])

        max_elevation = grid[0][0]
        min_heap = [(max_elevation, 0,0)]

        while min_heap:
            elevation, i, j = heapq.heappop(min_heap)

            if i == ROWS-1 and j == COLS-1:
                return elevation
            
            neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for x, y in neighbors:
                if min(x, y) < 0 or x >= ROWS or y >= COLS:
                    continue
                new_cost = max(elevation, grid[x][y])

                if new_cost < distance[x][y]:
                    distance[x][y] = new_cost
                    heapq.heappush(min_heap, (new_cost, x, y))


