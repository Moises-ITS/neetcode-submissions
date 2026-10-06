class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = set()
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                mp.remove(nums[l])
                l += 1
            if nums[r] in mp:
                return True
            
            mp.add(nums[r])
        return False