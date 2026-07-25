class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a adjency list 
        # loop through the list carrying a path
        # when you hit an empty node return true, and backtrack settting all nodes to [] since they are true
        adjList = {i: [] for i in range(numCourses)}
        for pre in prerequisites:
            adjList[pre[0]].append(pre[1])
        def dfs(node, path):
            if node in path: return False
            if adjList[node] == []:
                return True
            path.add(node)
            for pre in adjList[node]:
                if not dfs(pre, path):
                    return False
            adjList[node] = []
            return True
        for num in range(numCourses):
            if not dfs(num, set()): return False
        return True