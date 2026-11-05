class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        #pick is an arr of length n of False bools
        def dfs(subset, pick):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    subset.append(nums[i])
                    pick[i] = True
                    dfs(subset, pick)
                    subset.pop()
                    pick[i] = False
        dfs([], [False] * len(nums))
        return res