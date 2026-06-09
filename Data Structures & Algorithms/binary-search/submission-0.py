class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            midpoint = l + ((r-l)//2)
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                l += 1
            else:
                r -= 1
        return -1