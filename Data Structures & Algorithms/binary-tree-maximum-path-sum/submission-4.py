# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # keep a global max and work bottom up. 
        # calc the value of each subtree if a lower subtree is less than 0 drop it
        # update max every it return current val or 0
        maxPath = -float('inf')
        def dfs(node):
            if not node:
                return 0
            nonlocal maxPath
            leftSubTree = dfs(node.left)
            rightSubTree = dfs(node.right)
            maxSubTree = max(leftSubTree, rightSubTree, leftSubTree + rightSubTree)
            total = node.val + maxSubTree
            maxPath = max(total, maxPath, node.val)
            highestSubPath = max(node.val + leftSubTree, node.val + rightSubTree)
            return max(highestSubPath, node.val)
        dfs(root)
        return maxPath
        