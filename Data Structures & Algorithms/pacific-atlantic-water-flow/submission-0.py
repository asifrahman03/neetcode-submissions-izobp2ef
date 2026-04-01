class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited_pacific = set()
        visited_atlantic = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, ocean_set, prevHeight):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in ocean_set or heights[r][c] < prevHeight:
                return
            ocean_set.add((r,c))
            for x, y in directions:
                dfs(r + x, c + y, ocean_set, heights[r][c])


        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 or col == 0:
                    dfs(row, col, visited_pacific, heights[row][col])
                if row == ROWS-1 or col == COLS-1:
                    dfs(row, col, visited_atlantic, heights[row][col])
        
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visited_pacific and (r,c) in visited_atlantic:
                    res.append([r, c])
        return res