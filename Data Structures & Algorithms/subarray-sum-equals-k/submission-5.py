class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total, res = 0, 0
        mp = {0 : 1}

        for num in nums:
            total += num
            diff = total - k
            res += mp.get(diff, 0)
            mp[total] = mp.get(total, 0) + 1
        return res