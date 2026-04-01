class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def backtrack(start, curr_total, current):
            if curr_total == target:
                res.append(list(current))
                return
            for i in range(start, len(nums)):
                if curr_total + nums[i] > target:
                    continue
                current.append(nums[i])
                backtrack(i, curr_total + nums[i], current)
                current.pop()

        res = []
        nums.sort()
        backtrack(0, 0, [])

        return res

        
