class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create a global set the holds all number in range n
        # call dfs on every elemnt in the set when looking at an edge remove it from the global set
        # add a counter in the for each loop and return the value
        adj = {i: [] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        def dfs(node, prev):
            if node in visited:
                return 
            visited.add(node)
            if node == []:
                return 
            for edge in adj[node]:
                if edge == prev:
                    continue
                dfs(edge, node)
            return 
        visited = set()
        count = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i, -1)
            count += 1
        return count