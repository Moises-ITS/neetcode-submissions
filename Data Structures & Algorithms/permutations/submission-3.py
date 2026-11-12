class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(subset, pick):
            if len(subset) == len(nums):
                res.append(subset.copy())
            for j in range(len(nums)):
                if not pick[j]:
                    subset.append(nums[j])
                    pick[j] = True
                    dfs(subset, pick)
                    subset.pop()
                    pick[j] = False
        dfs([], [False] * len(nums))
        return res