class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, nums, total, subset):
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i >= len(candidates):
                return
            subset.append(nums[i])
            dfs(i + 1, nums, total + nums[i], subset)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1, nums, total, subset)
        dfs(0, candidates, 0, [])
        return res