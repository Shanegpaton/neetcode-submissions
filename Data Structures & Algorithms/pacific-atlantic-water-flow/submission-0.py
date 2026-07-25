class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # for every cell do a bfs every time search out into numbers less or equal to
        # once it hits the top or left set the pacific var to true and once it hits the atlantic set
        # alantic to true. if both are true add it to the result set
        res = []
        def dfs(row, col, path, touching, minHeight):
            if (row < 0 or col < 0 or row >= len(heights) 
                or col >= len(heights[row]) or (row, col) in path or heights[row][col] > minHeight):
                return 
            if row == 0 or col == 0:
                touching[0] = True
            if row == len(heights) - 1 or col == len(heights[row]) - 1:
                touching[1] = True
            if touching[0] and touching[1]:
                return
            path.add((row, col))
            minHeight = min(minHeight, heights[row][col])
            dfs(row + 1, col, path, touching, minHeight)
            dfs(row - 1, col, path, touching, minHeight)
            dfs(row, col + 1, path, touching, minHeight)
            dfs(row, col - 1, path, touching, minHeight)
        for row in range(len(heights)):
            for col in range(len(heights[row])):
                touching = [False, False]
                dfs(row, col, set(), touching, heights[row][col])
                if touching[0] and touching[1]:
                    res.append([row, col])
        return res