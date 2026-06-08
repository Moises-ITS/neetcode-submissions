class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        seen = set(nums)

        for num in seen:
            if num - 1 not in seen:
                long = 1
                while num+long in seen:
                    long += 1
                longest = max(longest, long)
        return longest
