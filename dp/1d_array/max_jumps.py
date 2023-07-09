from typing import List
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(len(nums))]
        maxi = 0

        for i in range(1,len(nums)):
            if nums[i]-nums[0]<=target and nums[i]-nums[0]>=-target:
                dp[i] = 1
        maxi = max(maxi, dp[-1]) 
        


        for i in range(1,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]-nums[i]<=target and nums[j]-nums[i]>=-target and dp[i]!=0:
                    dp[j] = max(dp[j], 1+dp[i])

            maxi = max(maxi, dp[-1])
            print(dp)
        
        if maxi!=0:
            return maxi
        
        return -1

'''
Problem : https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/
TC - (n ^ 2)
SC - O(n)
Approach : 
1.Initialize a dynamic programming array dp of the same length as nums, with all elements initially set to 0. This array will store the maximum number of jumps that can be made to reach each index.
2.Iterate over nums starting from the second element. For each element at index i, if the difference between nums[i] and nums[0] is within the target range, set dp[i] to 1, indicating that a jump from the first element to index i is possible.
3.Initialize a variable maxi to 0, which will keep track of the maximum number of jumps.
4.Iterate over nums from the second element to the second-to-last element. For each element at index i, iterate over the elements from i+1 to the last element. If the difference between nums[j] and nums[i] is within the target range and dp[i] is not 0 (indicating that a jump to index i is possible), update dp[j] to be the maximum of its current value and 1 + dp[i], indicating that a jump from index i to j is possible and increasing the maximum number of jumps at index j.
5.Update maxi to the maximum value of maxi and the last element of dp.
6.If maxi is not 0, return maxi as the maximum number of jumps. Otherwise, return -1 to indicate that no valid jumps are possible.

'''

print(Solution().maximumJumps(nums = [1,3,6,4,1,2], target = 0))