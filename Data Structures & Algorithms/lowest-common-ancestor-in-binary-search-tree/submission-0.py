# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p is on the other side of q return p
        # rec call on teh side that they are both on
        smaller = min(p.val, q.val)
        larger = max(p.val, q.val)
        if root.val <= larger and root.val >= smaller:
            return root
        if root.val > smaller:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)