"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        root = Node(node.val)
        visited[node] = root
        q = deque([node])
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    q.append(nei)
                visited[cur].neighbors.append(visited[nei])
        return visited[node]
            # create a queue and add the starting node
            # go through every neighbor add to the queue add each value to a "searched" dict
            # check if the value is in the searched dict for all edges and add it
            # with a deep copy
