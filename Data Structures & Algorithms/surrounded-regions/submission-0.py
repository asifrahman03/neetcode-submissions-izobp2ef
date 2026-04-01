class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or board[r][c] != 'O':
                return
            board[r][c] = '*'
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 or col == 0 or row == ROWS-1 or col == COLS-1:
                    if board[row][col] == 'O':
                        dfs(row, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == '*':
                    board[row][col] = 'O'


