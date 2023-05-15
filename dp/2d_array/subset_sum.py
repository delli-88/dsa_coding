# dp - Tabulation - Space Optimization
class Solution:
    def isSubsetSum (self, N, arr, sum):
        target = sum
        dp_prev = [False for _ in range(target+1)]


        dp_prev[0] = True
        
        # If we are pos 0, only that pos elemnt which if equals to target then it will be true
        if arr[0]<=target:
            dp_prev[arr[0]] = True
        
        # populating from row1,col1 to end
        for r in range(1,N):
            temp = [False for _ in range(target+1)]
            for c in range(1,target+1):

                pick = False
                if arr[r]<=c:
                    pick = dp_prev[c-arr[r]]
                
                no_pick = dp_prev[c]

                if pick or no_pick:
                    temp[c] = True
                else:
                    temp[c] = False
            dp_prev = temp

        return dp_prev[target]

'''
Problem : https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
TC - O(index * target)
SC - O(target)
Approach :
Same as tabulation, instead of matriix we just use an array of previous targets. 

'''

'''
# dp - Tabulation
class Solution:
    def isSubsetSum (self, N, arr, sum):
        target = sum
        dp = [[False for _ in range(target+1)] for _ in range(N)]


        # populating first column
        for row1 in range(N):
            dp[row1][0] = True
        
        # If we are pos 0, only that pos elemnt which if equals to target then it will be true
        if arr[0]<=target:
            dp[0][arr[0]] = True
        
        # populating from row1,col1 to end
        for r in range(1,N):
            for c in range(1,target+1):

                pick = False
                if arr[r]<=c:
                    pick = dp[r-1][c-arr[r]]
                
                no_pick = dp[r-1][c]

                if pick or no_pick:
                    dp[r][c] = True
                else:
                    dp[r][c] = False

        return dp[N-1][target]


TC - O(index * target)
SC - O(index * target)
Approach : 
We can store in a dp matrix of size index * target
For example,
dp[3][4] means, upto index 3 i.e from indices 0,1,2,3 is there any subset with tarhet==4
'''



'''
# dp - Memoization
class Solution:
    def isSubsetSum (self, N, arr, sum):
        dp = [[-1 for _ in range(sum+1)] for _ in range(N)]
        return self.isSubsetSumHelper(N-1,sum,arr, dp)


    def isSubsetSumHelper(self,pos,target,arr, dp):

        if target==0:
            dp[pos][target] = True
            return dp[pos][target]
        if pos==0:
            if target==arr[pos]:
                dp[pos][target] = True
                return dp[pos][target]
            else:
                dp[pos][target] = False
                return dp[pos][target]
        
        if dp[pos][target]!=-1:
            return dp[pos][target]


        pick = False
        if arr[pos]<=target:
            pick = self.isSubsetSumHelper(pos-1, target-arr[pos], arr, dp)        

        if pick:
            dp[pos][target] = True
            return dp[pos][target]
        
        no_pick = self.isSubsetSumHelper(pos-1, target, arr, dp)
        if no_pick:
            dp[pos][target] = True
            return dp[pos][target]
        

        dp[pos][target] = False
        return dp[pos][target]

TC - O(index * target)
SC - O(index * target) + O(index)
'''



print(Solution().isSubsetSum(4,[4,2,1,3],5))