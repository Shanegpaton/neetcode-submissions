# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order dfs returning the count + 1 every time we dont have a left
        # return the node when we hit count == k
        value = 0
        def dfs(node, k, count):
            nonlocal value
            if node.left:
                count = dfs(node.left, k, count)
            count += 1
            print(count)
            if count == k:
                value = node.val
            if node.right:
                count = dfs(node.right, k, count)
            return count
        dfs(root, k, 0)
        return value