class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #index, height
        res = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                j, h = stack.pop()
                res = max(res, h * (i - j))
                start = j
            stack.append((start, height))
        
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        return res