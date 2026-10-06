class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * (n * 2)
        for i in range(n * 2):
            ans[i] = nums[i % n] # 0 / 4 = 0, 4 % 4 = 0
        return ans