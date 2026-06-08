class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        post = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= post
            post *= nums[j]
        return res