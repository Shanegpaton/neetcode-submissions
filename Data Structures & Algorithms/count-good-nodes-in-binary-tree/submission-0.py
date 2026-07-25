# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # pre order dfs 
        nodeCounter = 0
        def dfs(node, highest):
            nonlocal nodeCounter
            if not node:
                return
            if node.val >= highest:
                highest = node.val
                nodeCounter += 1
            highest = max(highest, node.val)
            dfs(node.left, highest)
            dfs(node.right, highest)
        dfs(root, root.val)
        return nodeCounter

            