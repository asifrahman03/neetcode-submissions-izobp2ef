class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):
            if r < 0 or r >= len(grid):
                return 0
            if c < 0 or c >= len(grid[0]):
                return 0
            if grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            directions = [(0,1), (0,-1), (1, 0), (-1,0)]
            
            size = 1
            for x, y in directions:
                size += dfs(r + x, c + y)
            return size
            
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    curr_count = dfs(row, col)
                    res = max(res, curr_count)
        return res