# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # pre order dfs 
        def dfs(node, highest):
            if not node:
                return 0
            nodeCounter = 0
            if node.val >= highest:
                highest = node.val
                nodeCounter += 1
            nodeCounter += dfs(node.left, highest)
            nodeCounter += dfs(node.right, highest)
            return nodeCounter
        
        return dfs(root, root.val)

            