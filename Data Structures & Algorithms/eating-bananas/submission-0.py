import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #input: array and value
        #output: value
        #statically add piles[0] as base numbers
        #iterating through the list checking 2 conditions
        #keep in mind our k amount
        #1. piles[i] <= piles[0], piles[i] // piles[0] = count
        #2. if count > h, k += 1 and itertae through loop again
        #Edge Case: length is less than 1


        l, r = 1, max(piles)
        result = r
        while l <= r:
            k = (l + r) // 2
            time = 0
            for i in piles:
                time += math.ceil(i / k)
            if time <= h:
                result = k
                r = k -1
            else:
                l = k + 1
        return result

            