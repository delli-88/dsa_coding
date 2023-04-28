from typing import List
# dp - space - opt
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]==1 or obstacleGrid[0][0]==1:
            return 0
        
        prev = [-1 for _ in range(len(obstacleGrid[0]))]

        for r in range(len(obstacleGrid)):
            for c in range(len(obstacleGrid[0])):
                if r== 0 and c== 0:
                    prev[c] = 1
                else:
                    left = 0
                    if c>0 and obstacleGrid[r][c]!=1:
                        left = prev[c-1]
                    
                    up = 0
                    if r>0 and obstacleGrid[r][c]!=1:
                        up = prev[c]
                    
                    prev[c] = left+up
        return prev[-1]
'''
Problem : https://leetcode.com/problems/unique-paths-ii
TC - O(M*N)
SC - O(N)
Approach : 
Same as 'unique-paths-i' but instead of going from f(m-1, n-1) to f(0,0).
in this approach we are going from f(0,0) to f(m-1, n-1)
'''


'''
# dp - tabulation
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]==1 or obstacleGrid[0][0]==1:
            return 0
        
        dp= [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        for r in range(len(obstacleGrid)):
            for c in range(len(obstacleGrid[0])):
                if r== 0 and c== 0:
                    dp[r][c] = 1
                else:
                    left = 0
                    if c>0 and obstacleGrid[r][c]!=1:
                        left = dp[r][c-1]
                    
                    up = 0
                    if r>0 and obstacleGrid[r][c]!=1:
                        up = dp[r-1][c]
                    
                    dp[r][c] = left+up
        return dp[-1][-1]
'''


'''
# dp - memoization
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp= [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        return self.uniquePathsWithObstaclesHelper(obstacleGrid,len(obstacleGrid)-1,len(obstacleGrid[0])-1,dp)
    
    def uniquePathsWithObstaclesHelper(self,obstacleGrid,r,c,dp):
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]==1 or obstacleGrid[0][0]==1:
            return 0
        
        if r==0 and c==0:
            return 1

        if r<0 or c<0 or obstacleGrid[r][c]==1:
            return 0
        
        if dp[r][c]!=-1:
            return dp[r][c]
        
        left = self.uniquePathsWithObstaclesHelper(obstacleGrid,r,c-1,dp)
        up = self.uniquePathsWithObstaclesHelper(obstacleGrid,r-1,c,dp)

        dp[r][c] = left+up
        return dp[r][c]
'''



print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))