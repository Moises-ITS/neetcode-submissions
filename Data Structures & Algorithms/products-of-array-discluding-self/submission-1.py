class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [1] * len(nums)
        for i in range(len(nums)): #1, 1, 2, 8
            res[i] = prefix
            prefix *= nums[i]
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res