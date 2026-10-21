class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for start, stop in intervals[1:]:
            if res[-1][1] >= start:
                res[-1] = [
                    min(res[-1][0], start),
                    max(res[-1][1], stop)
                ] 
            else:
                res.append([start, stop])
        return res