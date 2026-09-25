class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = len(temperatures) * [0]
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t, j = stack.pop()
                res[j] = (i - j)
            stack.append([temp, i])
        return res