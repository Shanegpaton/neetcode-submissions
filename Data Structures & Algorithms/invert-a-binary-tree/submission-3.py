# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check null
        if not root:
            return
        # switch left and right
        temp = root.right
        root.right = root.left
        root.left = temp
        # call on left and right
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root