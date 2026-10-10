class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num - 1) not in numSet:
                long = 1
                while (num + long) in numSet:
                    long += 1
                longest = max(longest, long)
        return longest