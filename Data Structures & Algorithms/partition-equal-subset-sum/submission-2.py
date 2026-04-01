class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2
        memo = {}
        def dfs(i, remain):
            if remain == 0:
                return True
            if i >= len(nums) or remain < 0:
                return False
            if (i, remain) in memo:
                return memo[(i, remain)]
            
            # Two choices: include nums[i] OR skip nums[i]
            memo[(i, remain)] = (dfs(i + 1, remain - nums[i]) or 
                                dfs(i + 1, remain))
            return memo[(i, remain)]
        return dfs(0, half)