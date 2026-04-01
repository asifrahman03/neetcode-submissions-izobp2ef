class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_l = []
        p1 = 0
        p2 = 0
        # Creating merged sorted list
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                new_l.append(nums1[p1])
                p1 += 1
            else:
                new_l.append(nums2[p2])
                p2 += 1
        if p1 < len(nums1):
            while p1 < len(nums1):
                new_l.append(nums1[p1])
                p1 += 1
        if p2 < len(nums2):
            while p2 < len(nums2):
                new_l.append(nums2[p2])
                p2 += 1
        
        
        l = 0
        r = len(new_l) - 1
        mid = (l + r) // 2
        # Get median
        if len(new_l) % 2 == 0:
            return (new_l[mid] + new_l[mid+1]) / 2
        else:
            return new_l[mid]