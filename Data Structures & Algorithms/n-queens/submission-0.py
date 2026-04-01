class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [['Q']]


        res = []
        self.grid = [['.'] * n for _ in range(n)]
        self.cols = set()
        self.pos_diags = set()
        self.neg_diags = set()

        def backtrack(row):
            if row == n:
                res.append([''.join(r) for r in self.grid])
                return

            for col in range(n):
                if col not in self.cols and (row + col) not in self.pos_diags and (row - col) not in self.neg_diags:
                    self.grid[row][col] = 'Q'
                    self.cols.add(col)
                    self.pos_diags.add(row + col)
                    self.neg_diags.add(row - col)

                    backtrack(row+1)

                    self.grid[row][col] = '.'
                    self.cols.remove(col)
                    self.pos_diags.remove(row + col)
                    self.neg_diags.remove(row - col)
            # return []


        backtrack(0)
        return res


