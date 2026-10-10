class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        
        for key in mp:
            if mp[key] > len(nums) // 2:
                return key
        return -1