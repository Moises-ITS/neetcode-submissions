class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        total, res = 0, 0
        for num in nums:
            total += num
            diff = total - k
            res += mp.get(diff, 0)
            mp[total] = mp.get(total, 0) + 1
        return res
