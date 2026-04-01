class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # dp = [0] * n
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # if dp[1] == nums[1]:
        #     dp[0] = 0
        # for i in range(2, n):
        #     dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        results = [-1, -1]
        def houseRobber(start, finish, nums):
            prev2 = 0
            prev1 = 0
            for i in range(start, finish):
                curr = max(prev1, prev2 + nums[i])
                prev2 = prev1
                prev1 = curr
            return prev1
        results[0] = houseRobber(0, n-1, nums)
        results[1] = houseRobber(1, n, nums)
        return max(results[0], results[1])