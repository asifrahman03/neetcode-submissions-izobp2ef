class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        # visited = [False] * n

        def bt(index, curr_s):
            res.append(curr_s[:])
            for i in range(index, n):
                if i > index and nums[i-1] == nums[i]:
                    continue
                # if not check[i]:
                curr_s.append(nums[i])
                # visited[i] = True
                bt(i+1, curr_s)
                curr_s.pop()
                # visited[i] = False
            return

        # bt(0, [], visited)
        bt(0, [])
        return res