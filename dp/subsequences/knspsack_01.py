class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.

       
        # code here
    def knapSack(self,W, wt, val, n):

        dp = [-1 for _ in range(W+1)]
        # dp[0][0] = 0
        for r0 in range(W+1):
            if wt[0]<=r0:
                dp[r0] = val[0]
            else:
                dp[r0] = 0
        
        for i in range(1,len(wt)):
            for j in range(W,-1,-1):
                curr_wt = j
                profit_n = dp[j]
                profit_t = 0
                if wt[i]<=curr_wt:
                    profit_t = val[i] + dp[j-wt[i]]
                dp[j] = max(profit_n,profit_t)        
        return dp[-1]
    
'''
Approach :

1.Create a dynamic programming array dp of size W+1 and initialize all elements to -1. This array will store the maximum profit for each weight from 0 to W.
2.Initialize the base case for the first row of dp based on the weight and value of the first item. For each weight value r0 from 0 to W:
    2a.If the weight of the first item (wt[0]) is less than or equal to r0, set dp[r0] to the value of the first item (val[0]).
    2b.Otherwise, set dp[r0] to 0.
3.Iterate over the remaining items from index 1 to n-1:
    3a.For each item at index i, iterate over the weight values in reverse order from W to 0.
    3b.For each weight value j:
        3i.Calculate the current weight curr_wt as j.
        3ii.Get the current profit for the next item (profit_n) from dp[j].
        3iii.Calculate the potential profit for taking the current item (profit_t) as the sum of its value (val[i]) and the maximum profit for the remaining weight (dp[j-wt[i]]).
        4iv.Update dp[j] with the maximum of profit_n and profit_t.
4.After iterating over all items and weight values, the maximum achievable profit for the given weight limit W will be stored in dp[-1].
5.Return dp[-1] as the result.
'''
    #     dp = [[-1 for _ in range(W+1)] for _ in range(len(wt))]
    #     return self.helper(W,wt,val,n-1,dp)

    # def helper(self,W, wt, val, n, dp):
    #     if n==0:
    #         if wt[n]<=W:
    #             dp[n][W] = val[n]
    #             return dp[n][W]
    #         else:
    #             dp[n][W] = 0
    #             return dp[n][W]
    #     if dp[n][W]==-1:
    #         not_pick = self.helper(W,wt,val,n-1,dp)
    #     else:
    #         not_pick = dp[n][W]
    #     pick = -1
    #     if wt[n]<=W:
    #         if dp[n][W]==-1:
    #             pick = val[n] + self.helper(W-wt[n],wt,val,n-1,dp)
    #         else:
    #             pick = dp[n][W]
    #     return max(pick,not_pick)
            # dp = [[-1 for _ in range(W+1)] for _ in range(len(wt))]
            # return self.helper(W,wt,val,n-1,dp)
    
    # def helper(self,W, wt, val, n, dp):

    #     if dp[n][W]!=-1:
    #         return dp[n][W]
    #     if n==0:
    #         if wt[n]<=W:
    #             dp[n][W] = val[n]
    #             return dp[n][W]
    #         else:
    #             dp[n][W] = 0
    #             return dp[n][W]

    #     not_pick = self.helper(W,wt,val,n-1,dp)
    #     pick = -1
    #     if wt[n]<=W:
    #         pick = val[n] + self.helper(W-wt[n],wt,val,n-1,dp)
    #     dp[n][W] = max(pick,not_pick)
    #     return dp[n][W]
            
            # dp = [-1 for _ in range(W+1)]
            # # dp[0][0] = 0
            # for r0 in range(W+1):
            #     if wt[0]<=r0:
            #         dp[r0] = val[0]
            #     else:
            #         dp[r0] = 0
            
            # for i in range(1,len(wt)):
            #     curr = [-1 for _ in range(W+1)]
            #     for j in range(W+1):
            #         curr_wt = j
            #         profit_n = dp[j]
            #         profit_t = 0
            #         if wt[i]<=curr_wt:
            #             profit_t = val[i] + dp[j-wt[i]]
            #         curr[j] = max(profit_n,profit_t)
            #     dp = curr
            # return dp[-1]
            
