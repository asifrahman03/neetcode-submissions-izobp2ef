class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def bt(index, curr_set):
            if sum(curr_set) == target:
                res.append(curr_set[:])
                return
            for i in range(index, len(nums)):
                curr_set.append(nums[i])
                if sum(curr_set) < target:
                    bt(i, curr_set)
                else:
                    bt(i+1, curr_set)
                curr_set.pop()
        bt(0, [])
        return res
