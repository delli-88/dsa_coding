
from math import inf

# dp - tabulation
class Solution:
    def solve(self, n, m, grid):

        dp = [[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]

        for r in range(n-1,-1,-1):
            for c1 in range(m):
                for c2 in range(m):
                    if r==n-1:
                        if c1==c2:
                            dp[r][c1][c2] = grid[r][c1]
                        else:
                            dp[r][c1][c2] = grid[r][c1]+grid[r][c2]
                    else:

                        if c1==c2:
                            choco_count = grid[r][c1]
                        else:
                            choco_count = grid[r][c1]+grid[r][c2]

                        col_dirs = [-1,0,1]
                        maxi = 0

                        for i in range(3):
                            for j in range(3):
                                pickup = -inf
                                if c1+ col_dirs[i]>=0 and c1+ col_dirs[i]<m and c2+col_dirs[j]>=0 and c2+col_dirs[j]<m:
                                    pickup = dp[r+1][c1+ col_dirs[i]][c2+col_dirs[j]]
                                maxi = max(maxi, choco_count + pickup)
                        dp[r][c1][c2] = maxi
        return dp[0][0][-1]
'''
Problem : https://practice.geeksforgeeks.org/problems/chocolates-pickup/1
TC - O(N*M*M)*9
SC - O(N*M*M)
Approach:
We make both robots to travel simultaneously and return max
'''

'''
# dp - memoization
class Solution:
    def solve(self, n, m, grid):
        dp = [[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]
        return self.helper(0,0,m-1,grid,dp)

    def helper(self, r, c1, c2, grid, dp):
        row_len = len(grid)
        col_len = len(grid[0])
        if c1<0 or c1>=col_len or c2<0 or c2>=col_len:
            return -inf

        if r==row_len-1:
            if c1==c2:
                return grid[r][c1]
            return grid[r][c1]+grid[r][c2]
        
        if dp[r][c1][c2]!=-1:
            return dp[r][c1][c2]
        
        if c1==c2:
            choco_count = grid[r][c1]
        else:
            choco_count = grid[r][c1]+grid[r][c2]

        col_dirs = [-1,0,1]
        maxi = 0

        for i in range(3):
            for j in range(3):
                pickup = self.helper(r+1,c1+col_dirs[i],c2+col_dirs[j],grid,dp)

                maxi = max(maxi, choco_count + pickup)
        
        dp[r][c1][c2] = maxi
        return dp[r][c1][c2]

        
TC - O(N*M*M) * 9
SC -  O(N) + O(N*M*M)
'''







print(Solution().solve(4,3,[[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))
