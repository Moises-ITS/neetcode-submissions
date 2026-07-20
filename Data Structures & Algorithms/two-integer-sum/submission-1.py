class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            total = target - num
            if total in seen:
                return [seen[total], index]

            seen[num] = index