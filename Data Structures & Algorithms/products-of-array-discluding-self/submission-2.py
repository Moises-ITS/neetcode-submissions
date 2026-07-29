class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #1, 2, 4, 6
        #calucated 2 arrays 1 for prefix and 1 for postfix
        #multiply in place
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
        postfix = [1] * len(nums)
        for j in range(len(nums) - 2, - 1, -1):
            postfix[j] = nums[j+1] * postfix[j+1]

        res = [1] * len(nums)
        for k in range(len(nums)):
            res[k] = prefix[k] * postfix[k]
        return res