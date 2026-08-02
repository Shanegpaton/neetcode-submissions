# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return dfs(root.right, subRoot.right) and dfs(root.left, subRoot.left)
            else:
                return False
        if root and subRoot:
            if root.val == subRoot.val:
                if dfs(root, subRoot):
                    return True
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        return False



        
            



            
                