class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        heights.append(0)
        for i in range(len(heights)):
            start_index = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                res = max(res, height * (i - index))
                start_index = index
            stack.append((start_index, heights[i]))
        return res