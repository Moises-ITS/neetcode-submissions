class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        mp = {}
        for n in nums:
            mp[n] = mp.get(n, 0) + 1
        
        for num, count in mp.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(nums) - 1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return [nums[0]]