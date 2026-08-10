class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        temp = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:

            if start >= temp:
                temp = end
            else:
                res += 1
                temp = min(end, temp)
        return res
