class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(perms, pick):
            if len(perms) == len(nums):
                res.append(perms.copy())
            for i in range(len(nums)):
                if not pick[i]:
                    perms.append(nums[i])
                    pick[i] = True
                    dfs(perms, pick)
                    perms.pop()
                    pick[i] = False
        dfs([], [False] * len(nums))
        return res