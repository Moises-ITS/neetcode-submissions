class Solution:
    def jump(self, nums: List[int]) -> int:
        r = l = res = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            r = farthest
            l = i + 1
            res += 1
        return res