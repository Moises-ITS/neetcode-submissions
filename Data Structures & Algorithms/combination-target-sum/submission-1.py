class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #diff integers
        #target integer
        #all possible combinations to equal target like two sum
        res = []
        subset = []
        def dfs(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            if sum(subset) > target or i >= len(nums):
                return
            #since if statement is checking, no need to elsewhere
            subset.append(nums[i])
            dfs(i)

            subset.pop()
            dfs(i + 1)
            #add left or not, same with right
        dfs(0)
        return res 