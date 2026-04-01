class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_s = set(nums)
        currL = 0
        res = 0
        for n in new_s:
            if n - 1 not in new_s:
                currL = 1
                while n + currL in new_s:
                    currL += 1
                res = max(res, currL)

        return res