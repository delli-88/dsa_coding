class Solution:
    def cutRod(self, price, n):
        return self.cutRodMemoization(price,n)


    # DP - Tabulation 
    def cutRodTabulationSpaceOpt(self, price, n):
        dp = [[0 for _ in range(n+1)] for _ in range(len(price))]

        for i in range(n+1):
            dp[0][i] = price[0]*i

        for i in range(1,len(price)):
            for j in range(n+1):
                no_pick = dp[i-1][j]

                pick = 0
                if i+1 <= j:
                    pick = dp[i][j-(i+1)] + price[i]

                dp[i][j] = max(pick, no_pick)            

        return dp[-1][-1]
    '''
    Approach :
    1.Create a 2D dynamic programming array dp of size (len(price) x n+1) to store the maximum value obtainable for each rod length and each position.
    2.Initialize the first row of dp by considering only the first element in price and multiplying it by the rod length. This represents the maximum value obtainable when considering only the first element.
    3.Iterate through the remaining rows of dp starting from the second row.
    4.For each row, iterate through the rod lengths from 0 to n.
    5.Calculate the maximum value obtainable at each position by considering whether to pick or not pick the current element.
        a.The maximum value if not picking the current element is obtained from the value at the same position in the previous row, dp[i-1][j].
        b.The maximum value if picking the current element is obtained by subtracting (i+1) from the current rod length j and adding the price of the current element price[i].
        c.Choose the maximum value between the above two options and assign it to dp[i][j].
    6.After iterating through all rows and positions, the maximum value obtainable for the given rod length n is stored in dp[-1][-1].
    7.Return dp[-1][-1] as the result.
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
            



print(Solution().cutRod([1, 5, 8, 9, 10, 17, 17, 20],8))