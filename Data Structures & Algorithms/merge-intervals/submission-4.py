class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        pre = [intervals[0]]
        for start, stop in intervals[1:]:
            preEnd = pre[-1][1]
            if start <= preEnd:
                pre[-1][1] = max(preEnd, stop)
            else:
                pre.append([start, stop])
        return pre
            