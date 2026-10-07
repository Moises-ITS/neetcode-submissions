class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = {}
        minVal, maxVal = min(nums), max(nums)
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        index = 0
        for i in range(minVal, maxVal + 1):
            while count.get(i, 0) > 0:
                nums[index] = i
                index += 1
                count[i] -= 1
        return nums
