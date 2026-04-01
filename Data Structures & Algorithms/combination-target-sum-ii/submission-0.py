class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def bt(index, curr_set, curr_sum):
            if curr_sum == target:
                res.append(curr_set[:])
                return
            for i in range(index, len(candidates)):
                curr_n = candidates[i]
                if i > index and candidates[i-1] == candidates[i]:
                    continue
                if curr_n + curr_sum <= target:
                    curr_set.append(curr_n)
                    bt(i+1, curr_set, curr_n + curr_sum)
                    curr_set.pop()
        
        bt(0, [], 0)
        return res