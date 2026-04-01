class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')

        low = 0
        high = len(nums)-1
        while low <= high:
            if nums[low] < nums[high]:
                res = min(res, nums[low])
                break

            mid = (high+low) // 2
            res = min(res, nums[mid])
            if nums[low] <= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        return res