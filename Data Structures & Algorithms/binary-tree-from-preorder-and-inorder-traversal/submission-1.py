# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        # find the node in preorder and send everything on the left to the left tree
        # and everything on the right to the right tree
        middle = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: middle + 1], inorder[:middle])
        root.right = self.buildTree(preorder[middle + 1:], inorder[middle + 1:])
        return root        