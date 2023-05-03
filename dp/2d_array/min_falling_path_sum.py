from typing import List
from math import inf

# dp - Tabulation - space optimization
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        mat_len = len(matrix)
        min1 = inf
        prev = [-1 for _ in range(mat_len)]

        for r in range(mat_len-1,-1,-1):
            curr = [0 for _ in range(mat_len)]
            for c in range(mat_len-1,-1,-1):
                if r==mat_len-1:
                    prev[c] = matrix[r][c]
                    curr[c] = matrix[r][c]
                else:
                    left = inf
                    if c-1>=0:
                        left = prev[c-1]

                    right = inf
                    if c+1<mat_len:
                        right = prev[c+1]

                    down = prev[c]

                    curr[c] = matrix[r][c] + min(left, down, right)

                if r==0:
                    min1 = min(min1,curr[c])
            prev = curr
        return min1

'''
Problem : https://leetcode.com/problems/minimum-falling-path-sum
TC - O(row * col)
SC - O(col)
Approach:
same as tabulation, but instead of creating dp matrix of size (row*col)
we only create a dp array of size(col) and use this as prev
at every iteration we initialize the curr dp which stores curr min valus and 
at end of iteration we store this curr to prev array

'''

'''
# dp - Tabulation
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        mat_len = len(matrix)
        min1 = inf
        dp = [[-1 for _ in range(mat_len)] for _ in range(mat_len)]

        for r in range(mat_len-1,-1,-1):
            for c in range(mat_len-1,-1,-1):
                if r==mat_len-1:
                    dp[r][c] = matrix[r][c]
                else:
                    left = inf
                    if c-1>=0:
                        left = dp[r+1][c-1]

                    right = inf
                    if c+1<mat_len:
                        right = dp[r+1][c+1]

                    down = dp[r+1][c]

                    dp[r][c] = matrix[r][c] + min(left, down, right)

                if r==0:
                    min1 = min(min1,dp[r][c])
        
        return min1

# TC - O(row * col)
# SC - O(row * col)
Approach : 
This time we have to return the min of a path which can start from any row at 0 ind and can end at any row in last row
So we create a dp array of size [row][col]
we initializze the last row of dp with last row of matrix.
we loop through the matrix,
    if col in boundary, we take the minimum from left, down and right values from the below row 
    add it to curr matrix row col and store it in dp of curr_row and curr_col
at 0th row we have to find the minimim among them and return 
'''
                    

'''
# dp - Memoization
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        mat_len = len(matrix)
        min1 = inf
        dp = [[-1 for _ in range(mat_len)] for _ in range(mat_len)]
        for i in range(mat_len):
            self.minFallingPathSumHelper(matrix,0,i,dp,min1)
            min1 = min(min1,dp[0][i])
        return min1
    
    def minFallingPathSumHelper(self,matrix,r,c,dp,min1):
        mat_len = len(matrix)
        if r>=mat_len or c<0 or c>=mat_len:
            return inf
        if r==mat_len-1:
            dp[r][c] = matrix[r][c]
            return dp[r][c]
        if dp[r][c]!=-1:
            return dp[r][c]
        
        left = self.minFallingPathSumHelper(matrix,r+1,c-1,dp,min1)
        down = self.minFallingPathSumHelper(matrix,r+1,c,dp,min1)
        right = self.minFallingPathSumHelper(matrix,r+1,c+1,dp,min1)

        dp[r][c] = matrix[r][c] + min(left,down,right)
        return dp[r][c]

# TC - O()
# SC - O(row * col) + O(row)
'''


print(Solution().minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))