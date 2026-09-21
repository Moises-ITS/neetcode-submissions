class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, maxSum = 0, nums[0]
        for num in nums:
            if maxSub < 0:
                maxSub = 0
            maxSub += num
            maxSum = max(maxSub, maxSum)
        return maxSum
            