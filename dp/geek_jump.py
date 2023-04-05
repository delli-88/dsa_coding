# Tabulation Space Opt
from math import inf
class Solution:
    def minimumEnergy(self, height, n):
        dp = [0 for _ in range(n)]
        prev1 = 0
        prev2 = inf
        for jump in range(n-2,-1,-1):
            one_jump = abs(height[jump] - height[jump+1]) + prev1
            two_jump = inf
            if jump<n-2:
                two_jump = abs(height[jump] - height[jump+2]) + prev2
            dp[jump] = min(one_jump, two_jump)
            
            prev2 = prev1
            prev1 = dp[jump]
        return dp[0]

"""
Problem - https://practice.geeksforgeeks.org/problems/geek-jump/1
TC - O(n)
SC -O(1)
Approach:
For every step we have two options either to jump 1 step or to jump 2 steps
So we travel the array from right to left
at each step
    we calculate two things
        one_jump - which is the energy diff bw curr step and (curr_step + 1)  + the energy on scurr_tep + 1
        two_jump - which is the energy diff bw curr step and (curr_step + 2) + the energy on curr_step + 2
    then we can get the energy consumed in curr step by finding min of one_jump & two_jump
At 0 index we can get our solution
"""

# dp - Tabulation without Space Opt
"""
class Solution:
    def minimumEnergy(self, height, n):
        dp = [0 for _ in range(n)]
        for jump in range(n-2,-1,-1):
            one_jump = abs(height[jump] - height[jump+1]) + dp[jump+1]
            two_jump = inf
            if jump<n-2:
                two_jump = abs(height[jump] - height[jump+2]) + dp[jump+2]
            dp[jump] = min(one_jump, two_jump)
        return dp[0]
"""

# dp - memoization
"""
class Solution:
    def minimumEnergy(self, height, n):
        dp = [-1 for _ in range(n+1)]
        return self.minimumEnergyHelper(height,n-1,dp)

    def minimumEnergyHelper(self, height, pos, dp):

        if pos<=0:
            return 0
        
        if dp[pos]!=-1:
            return dp[pos]

        one_energy = abs(height[pos] - height[pos-1]) + self.minimumEnergyHelper(height, pos-1, dp)

        two_energy = inf
        if pos>1:
            two_energy =  abs(height[pos] - height[pos-2]) + self.minimumEnergyHelper(height, pos-2, dp)
        
        dp[pos] = min(one_energy,two_energy)
        return dp[pos]
"""


print(Solution().minimumEnergy([10,20,30,10],4))


