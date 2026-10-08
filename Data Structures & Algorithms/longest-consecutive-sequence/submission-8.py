class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for n in nums:
            if (n - 1) not in numSet:
                long = 1
                while (n + long) in numSet:
                    long += 1
                longest = max(longest, long)
        return longest