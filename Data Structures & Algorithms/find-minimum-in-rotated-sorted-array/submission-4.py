class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Input: list [nums]
        #Output: int
        #n = 6
        #[2, 3, 4-, 5, 6, 1]
        #[3,4,5-,6,1,2]
        #[4,5-,6,7]
        #[4,5,0,1,2,3]
        l = 0
        n = len(nums)
        r = n - 1
        lowest = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                lowest = min(lowest, nums[l])
                break
            m = l + (r - l) // 2
            lowest = min(lowest, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                lowest = min(lowest, nums[m])
                r = m - 1
        return lowest 


                
