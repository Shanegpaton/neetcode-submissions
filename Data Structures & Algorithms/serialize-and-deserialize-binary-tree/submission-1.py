# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        string = []
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    string.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
                else:
                    string.append("None")
               
        return ",".join(string)
# "1,2,3,None,None,None,None"         
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        nodes = deque(data.split(","))
        root = TreeNode(int(nodes.popleft()))
        tempList = deque([root])
        while tempList:
            for i in range(len(tempList)):
                node = tempList.popleft()
                leftVal, rightVal = nodes.popleft(), nodes.popleft()
                if leftVal != "None":
                    node.left = TreeNode(leftVal)
                    tempList.append(node.left)
                if rightVal != "None":
                    node.right = TreeNode(rightVal)
                    tempList.append(node.right)
        # for i in range len(node)
        # popleft from nodes and fill the other list with all non none nodes
        return root



