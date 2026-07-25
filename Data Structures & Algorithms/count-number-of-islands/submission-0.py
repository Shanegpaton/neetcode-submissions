class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if grid[row][col] == '0':
                return
            grid[row][col] = '0'
            #up 
            if row > 0:
                dfs(row - 1, col)
            #down 
            if row <= len(grid) - 2:
                dfs(row + 1, col)
            # left
            if col > 0:
                dfs(row, col - 1)
            #right
            if col <= len(grid[row]) - 2:
                dfs(row, col + 1)
        counter = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                print(grid[row][col])
                if grid[row][col] == '1':
                    counter += 1
                    dfs(row, col)
        return counter