# incorrect solution, needs to be modified
from math import inf
class Solution:
    def solve(self, n, m, grid):
        visited = [[0 for _ in range(m)] for _ in range(n)]
        robot1_first = self.helper(n,m,grid,visited,0,0,1)
        robot2_second = self.helper(n,m,grid,visited,0,m-1,0)
        choco_collection1 = robot1_first + robot2_second

        visited = [[0 for _ in range(m)] for _ in range(n)]
        robot2_first = self.helper(n,m,grid,visited,0,m-1,0)
        robot1_second = self.helper(n,m,grid,visited,0,0,1)
        choco_collection2 = robot2_first + robot1_second
       
        return max(choco_collection1,choco_collection2)
    
    def helper(self,n,m,grid,visited,r,c,robo):

        if r>n or c<0 or c>m:
            return 0
        
        if visited[r][c]==1:
            return 0

        if r==n-1:
            return grid[r][c]

        left = self.helper(n,m,grid,visited,r+1,c-1,robo)
        down = self.helper(n,m,grid,visited,r+1,c,robo)
        right = self.helper(n,m,grid,visited,r+1,c+1,robo)

        max_row = 0
        max_col = 0
        maxi = 0
        if robo:
            if left>maxi:
                maxi = left
                max_row = r+1
                max_col = c-1
            if down>maxi:
                maxi = down
                max_row = r+1
                max_col = c
            if right>maxi:
                maxi = right
                max_row = r+1
                max_col = c+1
        else:
            if right>maxi:
                maxi = right
                max_row = r+1
                max_col = c+1
            if down>maxi:
                maxi = down
                max_row = r+1
                max_col = c
            if left>maxi:
                maxi = left
                max_row = r+1
                max_col = c-1
        
        visited[max_row][max_col] = 1

        return grid[r][c] + maxi






print(Solution().solve(4,3,[[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))