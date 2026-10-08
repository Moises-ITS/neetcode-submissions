class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res, mp = [], {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        
        for key in mp:
            if mp[key] > len(nums) // 3:
                res.append(key)
        return res