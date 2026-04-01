class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c):
            if r < 0 or r >= len(grid):
                return 
            if c < 0 or c >= len(grid[r]):
                return 
            if grid[r][c] != '1':
                return 
            grid[r][c] = '0'
            directions = [(0, 1), (0, -1), (1, 0), (-1,0)]
            for x, y in directions:
                dfs(r + x, c + y)
            

        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    res += 1
                    dfs(row, col)
        return res
