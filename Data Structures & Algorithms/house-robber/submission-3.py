class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # if n >= 3:
        prev1 = 0
        prev2 = 0
        curr = 0
        for i in range(n):
            curr = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = curr
        
        return prev1