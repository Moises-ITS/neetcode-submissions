class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            pivot = l + (r - l) // 2
            if nums[pivot] < target:
                l = pivot + 1
            elif nums[pivot] > target:
                r = pivot - 1
            else:
                return pivot
        return -1

                
