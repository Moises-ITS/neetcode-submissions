class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for num, count in hashMap.items():
            freq[count].append(num)
        

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res 
