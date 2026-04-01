class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algo

        res = min(nums)
        cur = min(nums)
        for num in nums:
            if cur < 0:
                cur = 0
            cur += num
            res = max(res, cur)
        return res