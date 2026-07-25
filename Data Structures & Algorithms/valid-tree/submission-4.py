class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        nodes = set()
        def dfs(node, prev):
            if node in nodes:
                return False
            nodes.add(node)
            if adj[node] == []:
                return True
            for edge in adj[node]:
                if edge == prev:
                    continue
                if not dfs(edge, node): 
                    return False
            return True
        if not edges: return True
        cycle =  dfs(0, -1) 
        return cycle and len(nodes) == n
