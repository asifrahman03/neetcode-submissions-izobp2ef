class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1. Find max pile for binary search
        biggest = 0
        for num in piles:
            biggest = max(biggest, num)
        

        # 2. Binary search between 1 and biggest
        l = 1
        r = biggest
        res = float('inf')

        while l <= r:
            k = (r + l) // 2
            curr_time = 0
            for num in piles:
                if curr_time > h:
                    break
                curr_time += math.ceil(num / k)
            if curr_time <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
