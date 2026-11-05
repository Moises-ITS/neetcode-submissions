class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        freq = {}
        unique = []
        for c in candidates:
            freq[c] = freq.get(c, 0) + 1
            if c not in unique:
                unique.append(c)
        
        def dfs(nums, i, target, subset):
            if target == 0:
                res.append(subset.copy())
                return
            if target < 0 or i >= len(nums):
                return
            if freq[nums[i]]:
                subset.append(nums[i])
                freq[nums[i]] -= 1
                dfs(nums, i, target - nums[i], subset)
                freq[nums[i]] += 1
                subset.pop()
            dfs(nums, i + 1, target, subset)
        dfs(unique, 0, target, [])
        return res