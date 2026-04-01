class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums)-1
        if nums[l] <= nums[r]:
            res = nums[l]
            return res

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            # elif nums[mid] <= nums[l]:
            #     res = nums[mid]
            #     r = mid
            else:
                res = min(res, nums[mid])
                r = mid-1
        return res
        