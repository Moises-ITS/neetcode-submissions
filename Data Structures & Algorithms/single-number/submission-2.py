class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #a ^(XOR) a = 0 and a ^ 0 = a

        res = 0
        for num in nums:
            res = num ^ res
        return res
