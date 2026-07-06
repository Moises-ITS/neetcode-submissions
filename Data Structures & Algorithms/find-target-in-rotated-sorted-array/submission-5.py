class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums)
        r = n - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            #Using left and right pointers, we are able to conclude by using
            #left and right pointers and then by comparing two statements conjoined
            #with an & check first if num if less than midpoint, but greater than right then
            #remove right side of midpoint and isolate left, change midpoint and move right pointer

            if nums[l] <= nums[m]:          # left half is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:                            # right half is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
                    
                