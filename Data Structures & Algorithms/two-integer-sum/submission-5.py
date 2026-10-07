class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(nums):
            total = target - num
            if total in mp:
                return [mp[total], i]
            mp[num] = i