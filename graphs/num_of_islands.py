from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        visited = [[-1 for _ in range(col_len)] for _ in range(row_len)]

        islands_count = 0
        for i in range(row_len):
            for j in range(col_len):
                if visited[i][j]==-1 and grid[i][j]=="1":
                    islands_count+=1
                    self.visit_island(i,j,grid,visited)
        return islands_count

    def visit_island(self,r,c,grid,visited):
        row_len = len(grid)
        col_len = len(grid[0])

        if r<0 or r>=row_len or c<0 or c>=col_len:
            return
        
        if visited[r][c]==1 or grid[r][c]=="0":
            return
        
        r_dirs = [-1,0,1,0]
        c_dirs = [0,1,0,-1]

        visited[r][c] =1

        for v in range(4):
            self.visit_island(r+r_dirs[v],c+c_dirs[v],grid,visited)
        
        return




'''
Problem : https://leetcode.com/problems/number-of-islands/
TC - O(row * col)
SC - O(row * col) + O(row + col)
Approach :
We traverse through the grid,
    while traversing if we see an island, we inc island_count and vistit the entire island using dfs
    if we see an island which is visited or a sea we ignore

'''

print(Solution().numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))