class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        total = cur = 0

        for num in nums:
            total += num
            diff = total - k
            cur += (mp.get(diff, 0))
            mp[total] = mp.get(total, 0) + 1
        return cur