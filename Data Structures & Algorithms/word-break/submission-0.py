class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i):
            if i >= len(s):
                return True
            if i in memo:
                return memo[i]
            res = False
            for word in wordDict:
                if s.startswith(word, i, i+len(word)):
                    res |= dfs(i+len(word))
            memo[i] = res
            return res

        return dfs(0)