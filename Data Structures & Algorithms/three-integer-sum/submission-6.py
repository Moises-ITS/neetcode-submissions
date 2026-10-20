class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[l] + nums[i] + nums[r]
                if total == 0:
                    res.append([nums[l], nums[i], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return res