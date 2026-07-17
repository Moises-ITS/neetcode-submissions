import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        minHeap = self.nums
        heapq.heappush(minHeap, val)
        if len(minHeap) > self.k:
            heapq.heappop(minHeap)
        return minHeap[0]
