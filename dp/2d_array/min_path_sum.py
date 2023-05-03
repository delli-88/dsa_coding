from typing import List
from math import inf

# dp - Tabulation - Space Optimization
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        dp_down = [-1 for _ in range(len(grid[0]))]
        dp_right_ptr = inf
        for r in range(row_len-1,-1,-1):
            for c in range(col_len-1,-1,-1):
                if r==row_len-1 and c==col_len-1:
                    dp_down[c] = grid[r][c]
                    dp_right_ptr = grid[r][c]
                else:
                    right = inf
                    if c+1<col_len:
                        right = dp_right_ptr
                    
                    down = inf
                    if r+1<row_len:
                        down = dp_down[c]
                    
                    dp_down[c] = grid[r][c]+min(right,down)
                    dp_right_ptr = grid[r][c]+min(right,down)
        return dp_right_ptr    

'''
Problem : https://leetcode.com/problems/minimum-path-sum
TC - O(row * col)
SC - O(col)
Approach :
Similar to unique paths
At each element, we just find which is minimum either right or down and take it and add it to curr element
'''

'''
# dp - Tabulation
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for r in range(row_len-1,-1,-1):
            for c in range(col_len-1,-1,-1):
                if r==row_len-1 and c==col_len-1:
                    dp[r][c] = grid[r][c]
                else:
                    right = inf
                    if c+1<col_len:
                        right = dp[r][c+1]
                    
                    down = inf
                    if r+1<row_len:
                        down = dp[r+1][c]
                    
                    dp[r][c] = grid[r][c]+min(right,down)
        return dp[0][0]
'''
'''
TC - O(row * col)
SC - O(row * col)
'''



'''
# dp - Memoization
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        return self.minPathSumHelper(grid,0,0,dp)
    
    def minPathSumHelper(self,grid,row,col,dp):
        row_len = len(grid)
        col_len = len(grid[0])

        if row==row_len-1 and col == col_len-1:
            return grid[row_len-1][col_len-1]

        if row>=row_len or col>=col_len:
            return inf

        if dp[row][col]!=-1:
            return dp[row][col]
        
        right = self.minPathSumHelper(grid,row,col+1,dp)
        down = self.minPathSumHelper(grid,row+1,col,dp)

        dp[row][col] = grid[row][col] + min(right,down)

        return dp[row][col]
'''
'''
TC - O(N*M)
SC - O((M-1)+(N-1)) + O(N*M)
'''
    

print(Solution().minPathSum(grid = [[1,2,3],[4,5,6]]))