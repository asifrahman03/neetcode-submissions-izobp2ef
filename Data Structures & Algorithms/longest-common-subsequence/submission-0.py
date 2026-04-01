class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            tmp = text1
            text1 = text2
            text2 = tmp
        
        memo = {}
        res = 0
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            cur = 1
            if text1[i] == text2[j]:
                cur = max(cur, 1 + dfs(i+1, j+1))
            else:
                cur = max(dfs(i+1, j), dfs(i, j+1))
            memo[(i, j)] = cur
            return cur
            
        for i in range(len(text1)):
            res = max(res, dfs(i, i))
        return res

        