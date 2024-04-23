# https://leetcode.com/problems/number-of-islands/
# 2024-04-23

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_islands += 1
                    self.DFS(grid, i, j)
        
        return num_islands
    
    def DFS(self, grid, i, j):
        if i <0 or i>= len(grid) or j < 0 or j>=len(grid[0]):
            return
        if grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.DFS(grid, i+1, j)
        self.DFS(grid, i, j+1)
        self.DFS(grid, i-1, j)
        self.DFS(grid, i, j-1)

