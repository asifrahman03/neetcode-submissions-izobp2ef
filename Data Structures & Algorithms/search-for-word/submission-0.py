class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        visited = set()

        def bt(index, r, c):
            if index == len(word):
                return True
            if r < 0 or r >= ROW:
                return False
            if c < 0 or c >= COL:
                return False
            if board[r][c] != word[index] or (r, c) in visited:
                return False
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            temp = board[r][c]
            visited.add((r, c))
            for direction in directions:
                x, y = direction
                val = bt(index + 1, r + x, c + y)
                if val:
                    break
            board[r][c] = temp
            visited.remove((r, c))
            return val


        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == word[0]:
                    if bt(0, i, j):
                        return True
        return False