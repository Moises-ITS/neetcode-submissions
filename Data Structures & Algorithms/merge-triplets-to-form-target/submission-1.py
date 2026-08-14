class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False
        for i in triplets:
            x |= (i[0] == target[0] and i[1] <= target[1] and i[2] <= target[2])
            y |= (i[0] <= target[0] and i[1] == target[1] and i[2] <= target[2])
            z |= (i[0] <= target[0] and i[1] <= target[1] and i[2] == target[2])

        if not x or not y or not z:
            return False
        else:
            return True
        
