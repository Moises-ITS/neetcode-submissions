class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for num in numSet:
            if (num - 1) not in numSet:
                long = 1
                while (long + num) in numSet:
                    long += 1
                longest = max(longest, long)
        return longest