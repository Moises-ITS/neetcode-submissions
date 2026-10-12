class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = white = 0
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
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
        