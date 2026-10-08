class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * (2 * n)
        for i in range(n * 2):
            res[i] = nums[i % n]
        return res