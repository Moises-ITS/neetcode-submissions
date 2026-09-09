class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]: # if new interval comes before ith intervals
                res.append(newInterval)
                return res + intervals[i:]
            
            elif intervals[i][1] < newInterval[0]: #if new interval comes after ith interval
                res.append(intervals[i])
            else: #if new interval requires merging
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        res.append(newInterval)
        return res

