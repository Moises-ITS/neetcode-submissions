class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            total = target - num
            if total in hashMap:
                return [hashMap[total], i]
            hashMap[num] = i