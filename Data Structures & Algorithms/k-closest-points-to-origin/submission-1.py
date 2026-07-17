import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points: #point = [x, y]
            euDistance = x ** 2 + y ** 2
            distances.append([euDistance, x, y])
        heapq.heapify(distances)
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(distances)
            res.append([x, y])
        return res
