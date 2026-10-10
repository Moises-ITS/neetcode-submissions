class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white = 0, 0
        for color in nums:
            if color == 0:
                red += 1
            elif color == 1:
                white += 1
        
        for i in range(len(nums)):
            if red:
                nums[i] = 0
                red -= 1
            elif white:
                nums[i] = 1
                white -= 1
            else:
                nums[i] = 2

        