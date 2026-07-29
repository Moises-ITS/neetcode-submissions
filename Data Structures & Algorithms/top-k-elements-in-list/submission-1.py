class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        freq = [[] for i in range(len(nums) + 1)]

        for j in nums:
            hashMap[j] = hashMap.get(j, 0) + 1

        for num, count in hashMap.items():
            freq[count].append(num)

        res = []
        for h in range(len(freq) - 1, 0, -1):
            for num in freq[h]:
                res.append(num)
                if len(res) == k:
                    return res