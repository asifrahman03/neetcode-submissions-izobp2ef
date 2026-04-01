class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            # if nums[l] <= nums[r]:
            #     if target == nums[l]:
            #         return l
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if target >= nums[l] and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1 
