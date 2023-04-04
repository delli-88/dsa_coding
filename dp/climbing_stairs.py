class Solution:
    def climbStairs(self, n: int) -> int:

        #tabulation with space opt
        prev1 = 1
        prev2 = 1

        for _ in range(2,n+1):
            curr = prev1+prev2
            prev2 = prev1
            prev1 = curr
        return prev1
    
    """
    Problem : https://leetcode.com/problems/climbing-stairs/
    Approach : It will be similar to Fibonacci
    TC - O(n)
    SC - O(1) 
    """
    
    """
    memoization
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        return self.climbStairsHelper(n,dp)

    def climbStairsHelper(self,n,dp):
        if n==0:
            dp[0] = 1
            return dp[n]
        if n<0:
            return 0
        if dp[n]==-1:
            left =  self.climbStairsHelper(n-1,dp)
            right = self.climbStairsHelper(n-2,dp)
            dp[n] = left+right
        return dp[n]

        #tabulation
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
        """
    