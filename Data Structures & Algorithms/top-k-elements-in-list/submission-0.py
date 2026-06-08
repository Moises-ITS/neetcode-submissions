class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        freq = [[] for i in range(len(nums) + 1)]
        for i in nums:
            seen[i] = seen.get(i, 0) + 1
        for num, count in seen.items():
            freq[count].append(num)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return None