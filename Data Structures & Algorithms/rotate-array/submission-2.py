class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def rotate(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        n = len(nums)
        k %= n
        rotate(0, n - 1)
        rotate(0, k - 1)
        rotate(k, n - 1)
        