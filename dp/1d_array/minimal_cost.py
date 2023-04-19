from math import inf
class Solution:
    def minimizeCost(self, height, n, k):
        dp = [-1]*(n)
        dp[0] = 0

        for i in range(1,n):
            mini = inf
            for jump in range(1,k+1):
                if i-jump>=0:
                    mini = min(mini,abs(height[i]-height[i-jump])+ dp[i-jump])
            dp[i] = mini

        return dp[n-1]
    
"""
Problem : https://practice.geeksforgeeks.org/problems/minimal-cost/1
TC - O(n*k)
SC - O(n)
Optimal Approach: dp - Tabulation
Declare dp arr of size n
initialize base cond as dp[0] = 0
loop through arr from 1 to n-1
    at every index we again run a loop k times and calculate mini (mini is the min enery from the curr_index to curr_ind-k heights)
return dp[n-1]

"""



"""
# memoization
class Solution:
    def minimizeCost(self, height, n, k):
        dp = [-1]*n
        return self.minimizeCostHelper(height,n-1,k,dp)

    def minimizeCostHelper(self,height, n, k, dp):
        if n==0:
            dp[n] = 0
            return dp[n]
        if dp[n]!=-1:
            return dp[n]
        mini = 10001
        for jump in range(1,k+1):
            if n-jump>=0:
                mini = min(mini,abs(height[n]-height[n-jump])+ self.minimizeCostHelper(height,n-jump,k,dp))
        dp[n] = mini
        return dp[n]
"""



print(Solution().minimizeCost([10, 30, 40, 50, 20],5,3))