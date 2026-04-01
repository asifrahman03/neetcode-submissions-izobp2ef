class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algo

        res = float('-inf')
        cur = float('-inf')
        for num in nums:
            if cur < 0:
                cur = 0
            cur += num
            res = max(res, cur)
        return res