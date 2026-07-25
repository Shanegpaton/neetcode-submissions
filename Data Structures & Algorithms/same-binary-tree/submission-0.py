# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # search the trees in tandum
        # check if each value is equal. if not return fasle
        same = True
        def dfs(p, q):
            nonlocal same
            if not p or not q:
                if not p and q or not q and p:
                    same = False
                return
            if p.val != q.val:
                same = False
            dfs(p.left, q.left)
            dfs(p.right, q.right)
        dfs(p, q)
        return same
        # check the nodes are not none

        # check if the nodes are the same

        # look at the left node of each

        # look at the right node of each