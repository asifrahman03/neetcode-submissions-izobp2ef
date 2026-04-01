class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negated = [-num for num in stones]
        heapq.heapify(negated)

        while len(negated) > 1:
            val1 = -heapq.heappop(negated)
            val2 = -heapq.heappop(negated)
            res = abs(val1-val2)

            if res != 0:
                heapq.heappush(negated, -res)
            
        if len(negated) != 0:
            return -negated[0]
        return 0