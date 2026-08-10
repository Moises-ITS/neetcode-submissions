class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #search to see if newInterval[0] <= Interval[i][1]
        #if not add it to the end
        #if so find the interval to see if its overlapping with before and after
        #if so merge them
        #else place in middle
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(intervals[i][1], newInterval[1]),
                ]
        res.append(newInterval)
        return res
