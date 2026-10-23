class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #sorted in ascend -> 1, 2, 3
        l = 0
        r = len(nums) - 1
        while l < r:
            pivot = l + ((r - l) // 2)
            if nums[pivot] >= target:
                r = pivot
            elif nums[pivot] < target:
                l = pivot + 1
        return l if (l < len(nums) and nums[l] == target) else -1