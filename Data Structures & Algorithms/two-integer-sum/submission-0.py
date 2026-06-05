class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #3,4,5,6 target = 7
        # {3 : 0
        #   4: 1
        #   }

        hashMap = {}
        for i, num in enumerate(nums):
            res = target - num
            if res in hashMap:
                return [hashMap[res], i] 
            hashMap[num] = i
        return []
            
