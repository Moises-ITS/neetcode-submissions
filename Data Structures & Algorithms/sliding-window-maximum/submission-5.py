class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        max_li = [-heap[0][0]]
        for r in range(k, len(nums)):
            l = r - k + 1
            heapq.heappush(heap, (-nums[r], r))
            while heap and heap[0][1] < l:
                heapq.heappop(heap)
            max_li.append(-heap[0][0])
        return max_li
