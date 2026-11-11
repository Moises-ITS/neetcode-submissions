class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #banana eating rate of k 
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            m = l + (r-l) // 2
            t = 0
            for p in piles:
                t += math.ceil(float(p) / m)
            if t <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res