class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        memo = {}
        def dfs(start):
            if start >= len(s):
                return 1
            if start in memo:
                return memo[start]
            if s[start] == '0' or int(s[start]) < 0 or int(s[start]) > 26:
                return 0
            memo[start] = dfs(start+1) 
            if start+1 < len(s):
                num = s[start:start+2]
                if num[0] != '0' and int(num) <= 26:
                    memo[start] += dfs(start+2)
            return memo[start]

        return dfs(0)



