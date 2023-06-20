class Solution:
    def cutRod(self, price, n):
        return self.cutRodMemoization(price,n)


    # DP - Tabulation - Space Optimization
    def cutRodTabulationSpaceOpt(self, price, n):
        pass
    '''
    TC - O()
    SC - O()
    Approach :
    '''

    # DP - Tabulation
    def cutRodTabulation(self, price, n):
        pass

    '''
    TC - O()
    SC - O()
    Approach :
    '''

    # DP - Memoization
    def cutRodMemoization(self, price, n):
        dp = [[-1 for _ in range(n+1)] for _ in range(len(price)+1)]
        return self.cutRodMemoizationHelper(price,n,0,1,dp)
        
    def cutRodMemoizationHelper(self,price,n,cost,pos,dp):
        if pos>len(price) or n<=0:
            if n==0:
                return cost
            return -1
        if dp[pos][n]!=-1:
            return dp[pos][n]
        pick = self.cutRodMemoizationHelper(price,n-pos,cost+price[pos-1],pos,dp)
        no_pick = self.cutRodMemoizationHelper(price,n,cost,pos+1,dp)

        dp[pos][n] = max(pick, no_pick) 
        return dp[pos][n]
    '''
    TC - O()
    SC - O()
    Approach :
    '''

    # Recursion
    def cutRodRecursion(self, price, n):
        return self.cutRodRecursionHelper(price,n,0,1)
    def cutRodRecursionHelper(self,price,n,cost,pos):
        if pos>len(price) or n<=0:
            if n==0:
                return cost
            return -1

        pick = self.cutRodRecursionHelper(price,n-pos,cost+price[pos-1],pos)
        no_pick = self.cutRodRecursionHelper(price,n,cost,pos+1)

        return max(pick, no_pick)
            

    '''
    Problem : https://practice.geeksforgeeks.org/problems/rod-cutting0840/1
    TC - O()
    SC - O()
    Approach :
'''

print(Solution().cutRod([1, 5, 8, 9, 10, 17, 17, 20],8))