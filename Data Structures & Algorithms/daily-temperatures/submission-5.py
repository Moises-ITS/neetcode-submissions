class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #prevtemp, index
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                pt, j = stack.pop()
                res[j] = (i - j)
            stack.append([t, i])
        return res