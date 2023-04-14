# dp - Tabulation - space optimization
class Solution:
    def findMaxSum(self,arr, n):
        if n==1:
            return arr[0]
        
        prev2 = arr[-1]
        prev1 = max(arr[-2],prev2)

        for i in range(n-3,-1,-1):
            pick = arr[i] + prev2
            no_pick = 0 +  prev1
            prev2 = prev1
            prev1 = max(pick,no_pick)
        return prev1
    
'''
Problem : https://practice.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1
TC - O(n)
SC - O(1)
Optimal Approach:
We loop through the array from end
    at every index, we check which is maximum, 
    i) pick and add the curr element and add the index+2 element's subseq sum which we have stored in prev2
    ii) or Do not pick curr ele, directly take the subseq which is next to it, which is stored in prev1
    copy prev1 to prev2
    take max of pick or no_pick, and store it in prev1 to continue further
return prev1

'''

'''
# dp- Tabulation
class Solution:
    def findMaxSum(self,arr, n):
        dp = [-1]*n
        dp[-1] = arr[-1]
        dp[-2] = max(arr[-2],dp[-1])
        for i in range(n-3,-1,-1):
            pick = arr[i] + dp[i+2]
            no_pick = 0 +  dp[i+1]
            dp[i] = max(pick, no_pick)
        return dp[0]
            
# dp - memoization
class Solution:
    def findMaxSum(self,arr, n):
        return self.findMaxSumHelper(arr, n, 0, dp)

    def findMaxSumHelper(self, arr, n, pos, dp):
        if pos>=n:
            return 0

        if dp[pos]!=-1:
            return dp[pos]

        pick = arr[pos] + self.findMaxSumHelper(arr,n,pos+2, dp)
        no_pick = self.findMaxSumHelper(arr,n,pos+1, dp)

        dp[pos] = max(pick,no_pick)
        return dp[pos]
        

print(Solution().findMaxSum([5,5,10,100,10,5],6))
'''
print(Solution().findMaxSum([6,5,10,100,10,5],6))