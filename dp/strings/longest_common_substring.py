class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        return self.longestCommonSubstrTabSpaceOpt(S1, S2, n,m)
    
    def longestCommonSubstrTabSpaceOpt(self,s1, s2, n, m):
        prev = [0 for _ in range(m+1)]
        curr = prev[:]
        maxi = 0
        for i in range(1,n+1):
            for j in range(1, m+1):
                if s1[i-1]==s2[j-1]:
                    curr[j] = 1 + prev[j-1]
                    maxi = max(maxi, curr[j])
                else:
                    curr[j] = 0
            prev = curr[:]
        return maxi
    '''
    Problem : https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1
    TC - O(n * m)
    SC - O(m)
    Approach - Tabulation SpaceOpt
        same but instead of 2d array we have optiised to 1d
    '''
    
    def longestCommonSubstrTab(self, s1, s2, n, m):
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        maxi = 0
        for i in range(1,n+1):
            for j in range(1, m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    maxi = max(maxi, dp[i][j])
        return maxi
            
    '''
    TC - O(n * m)
    SC - O(n * m)
    Approach - Tabulation:
        1.Initialize a 2D array dp of size (n+1) * (m+1) with all elements set to 0. This array will store the lengths of the common substrings.
        2.Initialize a variable maxi to 0. This variable will keep track of the maximum length of the common substring encountered so far.
        3.Iterate through the strings s1 and s2 using two nested loops:
            AFor each i from 1 to n (inclusive):
                a.For each j from 1 to m (inclusive):
                    i.If s1[i-1] is equal to s2[j-1], it means we have found a matching character in both strings. In this case, set dp[i][j] to 1 plus the value of dp[i-1][j-1], representing the length of the common substring ending at the current positions of s1[i-1] and s2[j-1].
                    ii.Update maxi to the maximum value between maxi and dp[i][j], keeping track of the longest common substring encountered so far.
        4.Finally, return the value of maxi, which represents the length of the longest common substring found in s1 and s2.
    '''


print(Solution().longestCommonSubstr(S1 = "ABCDGH", S2 = "ACDGHR", n = 6, m = 6))