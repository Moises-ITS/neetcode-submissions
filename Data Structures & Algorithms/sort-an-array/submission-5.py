class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minVal, maxVal = min(nums), max(nums)
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        
        index = 0
        for val in range(minVal, maxVal + 1):
            while mp.get(val, 0) > 0:
                nums[index] = val
                index += 1
                mp[val] -= 1
        return nums