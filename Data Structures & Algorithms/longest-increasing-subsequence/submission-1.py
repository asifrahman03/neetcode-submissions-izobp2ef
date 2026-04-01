class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            curr = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    curr = max(curr, 1 + dfs(j))
            memo[i] = curr
            return curr
        
        for i in range(len(nums)):
            res = max(res, dfs(i))
        return res