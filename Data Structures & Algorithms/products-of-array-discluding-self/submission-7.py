class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        temp = nums[:]
        for i in range(len(temp)):
            temp[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(len(temp)-1, -1, -1):
            temp[i] *= post
            post *= nums[i]
        
        return temp
