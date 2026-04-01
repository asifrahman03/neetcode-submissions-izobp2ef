class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, curr_set):
            res.append(curr_set[:])
            for i in range(index, len(nums)):
                curr_set.append(nums[i])
                backtrack(i + 1, curr_set)
                curr_set.pop()
        
        backtrack(0, [])
        return res
        