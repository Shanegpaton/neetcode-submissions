# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check if the node in root == subroot if not left then right
        # if same check the roots left and right rec along with subroot and return false if diff
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            left, right = dfs(root.left, subRoot.left), dfs(root.right, subRoot.right)
            return left and right and root.val == subRoot.val
    
        if dfs(root, subRoot):
            return True
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
        return left or right


