class Solution:
    def FindMaxSum(self,a, n):
        prev1 = a[-1]
        prev2 = None
        for i in range(n-2,-1,-1):
            if i==n-2:
                pick = a[i]
            else:
                pick = a[i] + prev2

            no_pick = prev1

            curr = max(pick, no_pick)

            prev2 = prev1
            prev1 = curr
        
        return prev1

'''
Problem : https://practice.geeksforgeeks.org/problems/stickler-theif-1587115621/1
TC - O()
SC - O()
Optimal Approach : Same as max_sum_without_adjacents
'''
