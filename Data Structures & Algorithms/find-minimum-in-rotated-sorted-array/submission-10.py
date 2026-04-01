class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = float("infinity")


        while left <= right:
            if(nums[left] <= nums[right]):
                res = min(res, nums[left])
                break  # array already sorted
            mid = (left + right) // 2
            res = min(res, nums[mid])

            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return res

