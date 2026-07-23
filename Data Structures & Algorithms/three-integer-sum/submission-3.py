class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                ans = nums[l] + nums[r] + nums[i]
                if ans < 0:
                    l += 1
                elif ans > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[i], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
