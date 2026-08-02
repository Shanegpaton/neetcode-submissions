# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        smaller = min(p.val, q.val)
        larger = max(p.val, q.val)
        while root and (root.val < smaller or root.val > larger):
            if root.val > larger:
                root = root.left
            else:
                root = root.right
        return root