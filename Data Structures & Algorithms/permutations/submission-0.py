class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res= []
        n = len(nums)
        picked = [False] * n


        def bt(curr_s, p):
            if len(curr_s) == n:
                res.append(curr_s[:])
                return
            for j in range(n):
                if not p[j]:
                    curr_s.append(nums[j])
                    p[j] = True
                    bt(curr_s, p)
                    curr_s.pop()
                    p[j] = False
        
        bt([], picked)
        return res
