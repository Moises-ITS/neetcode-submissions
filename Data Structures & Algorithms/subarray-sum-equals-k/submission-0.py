class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = {0 : 1}

        tot = 0
        res = 0

        for num in nums:
            tot += num
            diff = tot - k
            res += hashMap.get(diff, 0)
            
            hashMap[tot] = hashMap.get(tot, 0) + 1
        
        return res