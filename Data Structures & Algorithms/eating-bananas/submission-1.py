import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #if min == len(piles) then answer is max(piles)
        res = 0
        l, r = 1, max(piles)
        while l <= r:
            m = l + ((r - l) // 2)

            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / m)
            if total_time <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
