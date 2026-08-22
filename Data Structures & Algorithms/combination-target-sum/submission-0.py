class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #backtracking is choice -> recurse -> undo -> next choice
        #The weird part of this problem is that we could have multiple nums[i] equal to target
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            #left
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            # right
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res 