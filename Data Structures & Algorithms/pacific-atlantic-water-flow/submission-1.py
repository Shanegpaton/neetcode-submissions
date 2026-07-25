class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(row, col, path, prevHeight):
            if (row < 0 or col < 0 or row >= len(heights) 
                or col >= len(heights[row]) or (row, col) in path or heights[row][col] < prevHeight):
                return 
            path.add((row, col))
            prevHeight = heights[row][col]
            dfs(row + 1, col, path, prevHeight)
            dfs(row - 1, col, path, prevHeight)
            dfs(row, col + 1, path, prevHeight)
            dfs(row, col - 1, path, prevHeight)

        pac = set()
        atl = set()
        #rows
        for row in range(len(heights)):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, len(heights[row]) - 1, atl, heights[row][len(heights[row]) - 1])        

        for col in range(len(heights[0])):
            dfs(0, col, pac, heights[0][col])
            dfs(len(heights) - 1, col, atl, heights[len(heights) - 1][col])

        for row in range(len(heights)):
            for col in range(len(heights[row])):
                if (row, col) in pac and (row, col) in atl:
                    res.append([row, col])
        return res