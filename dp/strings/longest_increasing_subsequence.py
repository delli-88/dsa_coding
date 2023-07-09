class Solution:
    def lengthOfLIS(self, nums):

        dp = [[-1 for _ in range(len(nums)+1)] for _ in range(len(nums))]
        return self.lengthOfLISMemoization(len(nums)-1,-1,nums,dp)

        # return self.lengthOfLISRecursion(len(nums)-1,-1,nums)
    
    def lengthOfLISTabSpaceOpt(self):
        return
    '''
    Problem : https://leetcode.com/problems/longest-increasing-subsequence/
    TC - O()
    SC - O()
    Approach - Tabulation SpaceOpt
    '''
    
    def lengthOfLISTab(self):
        return
    
    '''
    TC - O()
    SC - O()
    Approach - Tabulation
    '''
    def lengthOfLISMemoization(self, pos, prev, nums,dp):
        if pos<0:
            # if prev==-1:
            #     return 1
            # if nums[pos]<nums[prev]:
            #     return 1
            return 0
        
        if dp[pos][prev+1]!=-1:
            return dp[pos][prev+1]

        pick = 0
        if nums[pos]<nums[prev] or prev==-1:
            pick = 1+ self.lengthOfLISMemoization(pos-1,pos, nums,dp)

        no_pick = self.lengthOfLISMemoization(pos-1,prev, nums,dp)
        
        dp[pos][prev+1] = max(pick, no_pick)
        return dp[pos][prev+1]
    '''
    TC - O()
    SC - O()
    Approach - Memoization
    '''
    
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
    '''
    TC - O()
    SC - O()
    Approach - Recursion
    '''


print(Solution().lengthOfLIS(nums = [1,3,6,7,9,4,10,5,6]))

