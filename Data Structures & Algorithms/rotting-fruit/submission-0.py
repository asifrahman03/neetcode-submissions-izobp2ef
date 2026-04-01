class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        good_fruit = 0

        def processMin(r, c):
            nonlocal good_fruit
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r,c) in visited:
                return 
            if grid[r][c] != 1:
                return 
            visited.add((r,c))
            q.append([r, c])
            grid[r][c] = 2
            good_fruit -= 1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    good_fruit += 1
                elif grid[row][col] == 2:
                    visited.add((row, col))
                    q.append([row, col])
        
        mins = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                processMin(r+1, c)
                processMin(r-1, c)
                processMin(r, c-1)
                processMin(r, c+1)
            if q:
                mins += 1
        # if good_fruit > 0:
        #     return -1
        return -1 if good_fruit > 0 else mins


                
