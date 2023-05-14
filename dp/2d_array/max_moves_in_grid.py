from typing import List

# dp - Tabulation - Space Optimization
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        dp_prev = [-1 for _ in range(len(grid))]
        maxi = 0

        for c in range(col_len-1,-1,-1):
            temp = [-1 for _ in range(len(grid))]
            for r in range(row_len-1,-1,-1):

                if c==col_len-1:
                    dp_prev[r]=1
                    temp[r] = 1

                else:
                    diag_up = 0
                    if r-1>=0 and c+1<=col_len and grid[r][c]<grid[r-1][c+1]:
                        diag_up = dp_prev[r-1]

                    right = 0
                    if c+1<=col_len and grid[r][c]<grid[r][c+1]:
                        right = dp_prev[r]

                    diag_down =0
                    if r+1<row_len and c+1<=col_len and grid[r][c]<grid[r+1][c+1]:
                        diag_down = dp_prev[r+1]
                    
                    temp[r] = max(diag_up, right, diag_down)

                    if c!=0:
                        temp[r]+=1
                    else:
                        maxi = max(maxi,temp[r])
            dp_prev = temp

        return maxi
'''
Problem : https://leetcode.com/problems/maximum-number-of-moves-in-a-grid
TC - O(r * c)
SC - O(r)
Approach :
Same as 2d dp grid, but in this case, the inner loop is for rows and outer is for cols
'''


'''
# dp - Tabulation
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        maxi = 0

        for c in range(col_len-1,-1,-1):
            for r in range(row_len-1,-1,-1):

                if c==col_len-1:
                    dp[r][c]=1

                else:
                    diag_up = 0
                    if r-1>=0 and c+1<=col_len and grid[r][c]<grid[r-1][c+1]:
                        diag_up = dp[r-1][c+1]

                    right = 0
                    if c+1<=col_len and grid[r][c]<grid[r][c+1]:
                        right = dp[r][c+1]

                    diag_down =0
                    if r+1<row_len and c+1<=col_len and grid[r][c]<grid[r+1][c+1]:
                        diag_down = dp[r+1][c+1]
                    
                    dp[r][c] = max(diag_up, right, diag_down)

                    if c!=0:
                        dp[r][c]+=1
                    else:
                        maxi = max(maxi,dp[r][c])

        return maxi
'''
    

'''
# dp - Memoization
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        maxi = 0
        dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            move = self.maxMovesHelper(grid,i,0,dp)
            maxi = max(maxi, move-1)
            print(dp)
        return maxi
        

    def maxMovesHelper(self,grid,r,c,dp):

        max_row = len(grid)
        max_col = len(grid[0])

        if c==max_col-1:
            dp[r][c] = 1
            return dp[r][c]

        if dp[r][c]!=-1:
            return dp[r][c]

        maxi = 0
        
        for row in range(-1,2): # i = -1, 0, 1

            if r+row>=0 and r+row <max_row and c+1<max_col and grid[r][c]<grid[r+row][c+1]:
                move = self.maxMovesHelper(grid,r+row,c+1,dp)
                maxi = max(maxi,move)
        
        dp[r][c] = 1+maxi        
        return dp[r][c]
'''





print(Solution().maxMoves(grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))

