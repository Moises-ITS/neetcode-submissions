class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums) - 1
        l, r = 0, n
        while l < r:
            m = l + (r-l) // 2
            if nums[m] < nums[r]:
                #means right side is less than left
                r = m
            else:
                l = m + 1
                #arry is sorted
        return nums[l]