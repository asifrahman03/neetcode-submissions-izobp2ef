class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        total = len(A) + len(B)
        half = total // 2
        if len(A) > len(B):
            A, B = B, A
        
        l = 0
        r = len(A) - 1
        while True:
            mid = (l + r) // 2
            B_part = half - mid - 2

            A_left = A[mid] if mid >= 0 else float('-inf')
            B_left = B[B_part] if B_part >= 0 else float('-inf')
            A_right = A[mid+1] if (mid+1) < len(A) else float('inf')
            B_right = B[B_part+1] if (B_part+1) < len(B) else float('inf')

            if A_left <= B_right and B_left <= A_right:
                if total % 2 != 0:
                    return min(A_right, B_right)
                else:
                    left_max = max(A_left, B_left)
                    right_min = min(A_right, B_right)
                    res = (left_max + right_min) / 2
                    return res
            elif A_left > B_right:
                r = mid - 1
            else:
                l = mid + 1