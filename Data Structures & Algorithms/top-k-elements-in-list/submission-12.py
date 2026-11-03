class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1
        for num, count in m.items():
            freq[count].append(num)
        res = []
        for i in range(len(nums) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return [nums[0]]