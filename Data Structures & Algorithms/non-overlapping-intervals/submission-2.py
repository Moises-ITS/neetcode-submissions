class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x: x[1])
        prevEnd = float("-inf")
        for start, stop in intervals:
            if start < prevEnd:
                count += 1
            else:
                prevEnd = stop
        return count