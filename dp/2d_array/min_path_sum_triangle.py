from typing import List
from math import inf
# dp - Tabulation - Space Optimization
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [-1 for _ in range(len(triangle[-1]))]
        row_len = len(triangle)
        for r in range(row_len-1,-1,-1):
            col_len = r+1
            col_to_check = len(triangle[-1])-1
            for c in range(col_len-1,-1,-1):
                if r==row_len-1:
                    dp[c]=triangle[r][c]
                else:
                    next_row_1 = 0
                    next_row_2 = 0
                    if r+1<row_len:
                        next_row_1 = dp[col_to_check]
                    if r+1<row_len and c+1<=col_len:
                        next_row_2 = dp[col_to_check-1]
                    
                    dp[col_to_check] = triangle[r][c] + min(next_row_1,next_row_2)
                    col_to_check-=1
        return dp[-1]       

'''
Problem : https://leetcode.com/problems/triangle
TC - O(row * col)
SC - O(lastColumn)
Approach :
Same as min Path sum
in this instead we travel down and diagonally and the column len varies
'''

'''
# dp - tabulation
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[-1 for _ in range(r+1)] for r in range(len(triangle))]

        row_len = len(triangle)
        for r in range(row_len-1,-1,-1):
            col_len = r+1
            for c in range(col_len-1,-1,-1):
                next_row_1 = 0
                next_row_2 = 0
                if r+1<row_len:
                    next_row_1 = dp[r+1][c]
                if r+1<row_len and c+1<=col_len:
                    next_row_2 = dp[r+1][c+1]
                
                dp[r][c] = triangle[r][c] + min(next_row_1,next_row_2)
        return dp[0][0]

# TC - O(row * col)
# SC - O(row * col)
'''



'''
# dp - Memoization
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[-1 for _ in range(r+1)] for r in range(len(triangle))]

        return self.minimumTotalHelper(triangle,0,0,dp)
    
    def minimumTotalHelper(self,triangle,r,c,dp):
        row_len = len(triangle)-1
        col_len = r+1
        if r>row_len or c>col_len:
            return 0
        
        if dp[r][c]!=-1:
            return dp[r][c]
        
        next_row_1 = self.minimumTotalHelper(triangle,r+1,c,dp)
        next_row_2 = self.minimumTotalHelper(triangle,r+1,c+1,dp)

        dp[r][c] = triangle[r][c]+ min(next_row_1,next_row_2)

        return dp[r][c]

#TC - O(row*col)
#SC - O(row) + O(row * col)        
'''


print(Solution().minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))


