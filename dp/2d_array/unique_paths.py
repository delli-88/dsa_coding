# dp - tabulation - space_optimization

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_down = [-1 for _ in range(n)]
        for r in range(m-1,-1,-1):
            dp_right = 0
            for c in range(n-1,-1,-1):
                if (r==m-1 and c==n-1):
                    dp_right = 1
                    dp_down[c] = 1
                    continue
                right = dp_right
                if r+1<m:
                    down = dp_down[c]
                else:
                    down = 0
                dp_down[c] = right+down
                dp_right = right+down
        return dp_right
    
'''
Problem : https://leetcode.com/problems/unique-paths
TC - O()
SC - O()
Approach : 
'''


'''
# dp - tabulation
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):

                if r==m-1 and c==n-1:
                    dp[r][c] = 1

                else:
                    if c+1<n:
                        right = dp[r][c+1]
                    else:
                        right = 0
                    
                    if r+1<m:
                        down = dp[r+1][c]
                    else:
                        down = 0

                    dp[r][c] = right+down
        return dp[0][0]
'''


'''
# dp - Memoization
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.uniquePathsHelper(0,0,m,n,dp)
        
    def uniquePathsHelper(self,r,c,m,n,dp):
        if r==m-1 and c==n-1:
            return 1

        if r>=m or r<0 or c>=n or c<0:
            return 0

        if dp[r][c] !=-1:
            return dp[r][c]

        right = self.uniquePathsHelper(r,c+1,m,n,dp)
        down = self.uniquePathsHelper(r+1,c,m,n,dp)

        dp[r][c] = right+down

        return dp[r][c]
'''
'''
TC - O(M*N)
SC - O((N-1)+(M-1)) + O(M*N)
Approach : 
'''

# print(Solution().uniquePaths(3,7))