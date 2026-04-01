class Solution:
    def binarySearch(self, row, target):
        l = 0
        r = len(row)-1

        while l <= r:
            m = l + ((r-l)//2)

            if row[m] == target:
                return True
            elif row[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1

        while left <= right:
            row = left + ((right - left)//2)
            print(matrix[row])

            if matrix[row][0] <= target and matrix[row][-1] >= target:
                res = self.binarySearch(matrix[row], target)
                return res
            elif matrix[row][0] < target:
                left = row + 1
            else:
                right = row - 1
        return False
