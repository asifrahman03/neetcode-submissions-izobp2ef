class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = 1
        curMin = 1

        for num in nums:
            p_max = curMax * num
            curMax = max(num, p_max, num * curMin)
            curMin = min(num, p_max, num * curMin)
            res = max(res, curMax)
        return res