# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #left subtree of every node contains keys less than node's key
        #right subtree of every node contains keys less than node's key
        #both left and right are also bst
        def dfs(root, left, right):
            if not root:
                return True
            if not (left < root.val and root.val < right):
                return False
            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
        
        return dfs(root, float("-inf"), float("inf"))