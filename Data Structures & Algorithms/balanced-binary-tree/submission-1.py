# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # hold an array valid and height
        def dfs(node):
            if not node:
                return [True, 0]
            validL, left = dfs(node.left)
            validR, right = dfs(node.right)
            valid = abs(left - right) <= 1 and validR and validL
            return [valid, max(left, right) + 1]
        return dfs(root)[0]