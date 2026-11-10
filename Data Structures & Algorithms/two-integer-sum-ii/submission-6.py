class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(numbers):
            total = target - num
            if total in hashMap:
                return [hashMap[total] + 1, i + 1]
            hashMap[num] = i