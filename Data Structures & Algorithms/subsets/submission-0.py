#You will always have 2^n solutions where n is length of nums
#2 numbers = 4 solutions
#3 numbers = 8 solutions
#4 numbers = 16 solutions
#[]
#[1], [1, 2], [1, 3], [1, 4], [1, 2, 3], [1, 3, 4], [1, 2, 4], [1, 2, 3, 4]
#[2], [2, 3], [2, 4], [2, 3, 4]
#[3], [3, 4]
#[4]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            #left decision
            subset.append(nums[i])
            dfs(i + 1)

            #decision NOT to include nums[i] aka right decision
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res