# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, left, right):
            #left has to be range(float(-inf)->ceiling(root.node))
            #right has to be range(floor(root.node)->float(inf))
            if not root:
                return True
            if not (left < root.val < right):
                return False
            return (
                dfs(root.left, left, root.val) and
                dfs(root.right, root.val, right)
            )
        return dfs(root, float("-inf"), float("inf"))