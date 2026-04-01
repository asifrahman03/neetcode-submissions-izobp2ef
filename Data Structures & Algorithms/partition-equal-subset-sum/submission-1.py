class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2
        memo = {}

        def dfs(i, remain):
            if (i, remain) in memo:
                return memo[(i, remain)]
            if remain - nums[i] == 0:
                return True
            elif remain - nums[i] < 0:
                return False
            new_remain = remain - nums[i]
            for j in range(i+1, len(nums)):
                if (dfs(j, remain) or dfs(j, new_remain)):
                    memo[(i, remain)] = True
                    return True
            memo[(i, remain)] = False
            return False

        return dfs(0, half)