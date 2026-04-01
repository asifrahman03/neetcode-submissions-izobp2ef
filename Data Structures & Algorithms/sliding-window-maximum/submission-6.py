class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 1:
            return nums
        res = []
        l = 0
        max_h = []
        for r in range(len(nums)+1):
            while r - l + 1 > k:
                while max_h[0][1] < l:
                    heapq.heappop(max_h)
                res.append(-max_h[0][0])
                l += 1
                if max_h[0][1] < l:
                    heapq.heappop(max_h)
            if r == len(nums):
                break
            heapq.heappush(max_h, [-nums[r], r])
        return res