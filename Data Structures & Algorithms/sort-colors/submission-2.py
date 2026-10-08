class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white = 0, 0
        for n in nums:
            if n == 0:
                red += 1
            elif n == 1:
                white += 1
        
        for i in range(len(nums)):
            if red:
                red -= 1
                nums[i] = 0
            elif white:
                white -= 1
                nums[i] = 1
            else:
                nums[i] = 2