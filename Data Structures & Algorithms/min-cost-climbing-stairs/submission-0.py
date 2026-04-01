class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0] * (len(cost) + 1)
        for i in range(len(cost)):
            memo[i] = cost[i]
        memo[-1] = 0

        for i in range(len(memo)-3, -1, -1):
            memo[i] = memo[i] + min(memo[i+1], memo[i+2])
        
        return min(memo[0], memo[1])

        # memo

        # def dfs(i):
        #     if i >= len(memo)-1:
        #         return 
        #     if memo[i] != 0:
        #         return memo[i]
        # # for j in range(i, len(memo)):
        #     memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
        #     return memo[i]
        
        # return memo[len(cost)-1]