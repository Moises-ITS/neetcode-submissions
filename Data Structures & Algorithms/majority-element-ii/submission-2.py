class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp, res = {}, []
        for n in nums:
            mp[n] = mp.get(n, 0) + 1
        
        for key in mp:
            if mp[key] > len(nums) // 3:
                res.append(key)
        return res