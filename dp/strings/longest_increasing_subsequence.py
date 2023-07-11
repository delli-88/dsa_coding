class Solution:
    def lengthOfLIS(self, nums):

        return self.lengthOfLISTabSpaceOpt(nums)
        # dp = [[-1 for _ in range(len(nums)+1)] for _ in range(len(nums))]
        # return self.lengthOfLISMemoization(0,-1,nums,dp)

        # return self.lengthOfLISRecursion(len(nums)-1,-1,nums)
    def printLIS(self, nums):
        lis_len, dp = self.lengthOfLIS(nums)
        lis = [0 for _ in range(lis_len)]
        ptr = lis_len
        prev = -1
        for i in range(len(dp)-1,-1,-1):
            if  (dp[i]==ptr and prev==-1) or (dp[i]==ptr and nums[i]<prev):
                lis[ptr-1] = nums[i]
                prev = nums[i]
                ptr -= 1
        return lis

    def lengthOfLISTabSpaceOpt(self, nums):
        dp = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            maxi = dp[i]
            for j in range(i):
                if nums[i]>nums[j]:
                    maxi = max(maxi, 1+dp[j])
            dp[i] = maxi
        return (max(dp),dp)
        # return (max(dp),dp)# for printLIS

    
    def lengthOfLISTab(self, nums):
        dp = [[0 for _ in range(len(nums)+1)] for _ in range(len(nums)+1)]
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i-1,-2,-1):
                pick = 0
                if nums[i]>nums[j] or j==-1:
                    pick = 1+ dp[i+1][i+1]
                no_pick = dp[i+1][j+1]
                dp[i][j+1] = max(pick, no_pick)

        return dp[0][-1+1]
    
    def lengthOfLISMemoization(self, pos, prev, nums,dp):
        if pos==len(nums):
            return 0
        
        if dp[pos][prev+1]!=-1:
            return dp[pos][prev+1]

        pick = 0
        if nums[pos]>nums[prev] or prev==-1:
            pick = 1+ self.lengthOfLISMemoization(pos+1,pos, nums,dp)

        no_pick = self.lengthOfLISMemoization(pos+1, prev, nums,dp)
        
        dp[pos][prev+1] = max(pick, no_pick)
        return dp[pos][prev+1]

    def lengthOfLISRecursion(self, pos, prev, nums):
        if pos==0:
            if prev==-1:
                return 1
            if nums[pos]<nums[prev]:
                return 1
            return 0


        pick = 0
        if nums[pos]<nums[prev] or prev==-1:
            pick = 1+ self.lengthOfLISRecursion(pos-1,pos, nums)

        no_pick = self.lengthOfLISRecursion(pos-1,prev, nums)
            
        return max(pick, no_pick)

# print(Solution().lengthOfLIS(nums = [1,3,6,7,9,4,10,5,6]))
print(Solution().printLIS(nums = [0,1,0,3,2,3]))

