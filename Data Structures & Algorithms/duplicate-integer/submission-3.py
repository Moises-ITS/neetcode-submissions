class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        hashMap = {}
        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1
        return False if max(hashMap.values()) < 2 else True