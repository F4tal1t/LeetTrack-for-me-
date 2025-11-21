class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n, noOfIslands= len(grid), len(grid[0]), 0

        def bfs(row,col):
            if 0<=row<m and 0<=col<n and grid[row][col] == "1":
                grid[row][col] = "0"
            else:
                return
            bfs(row+1,col)
            bfs(row-1,col)
            bfs(row,col+1)
            bfs(row,col-1)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    bfs(row,col)
                    noOfIslands += 1
        return noOfIslands