# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       # pre order dfs
       # check that the node is within the left and right boundry
       # look at left and right and ensure left < root and right > root
        #update the boundries so right is the right most value on right 
        def dfs(node, left, right):
            if not node:
                return True
            if node.val <= left or node.val >= right:
                return False
            lValid = dfs(node.left, left, node.val)
            rValid = dfs(node.right, node.val, right)
            return lValid and rValid
        return dfs(root, -float('inf'), float('inf'))