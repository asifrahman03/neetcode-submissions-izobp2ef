class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algo

        res = 0
        for num in nums:
            if res < 0:
                res = 0
            res += num
        return res