class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count, res = {}, []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key in count:
            if count[key] > len(nums) // 3:
                res.append(key)
        return res
        
