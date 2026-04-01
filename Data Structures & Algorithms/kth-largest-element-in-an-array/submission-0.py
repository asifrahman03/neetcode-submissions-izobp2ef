class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negated = [-num for num in nums]

        heapq.heapify(negated)

        while k != 1:
            heapq.heappop(negated)
            k -= 1
        
        return -negated[0]