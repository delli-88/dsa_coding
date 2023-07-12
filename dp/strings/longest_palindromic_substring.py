class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[True for _ in range(len(s))] for _ in range(len(s))]

        maxi = 0
        
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    maxi = max(maxi, j-i+1)
                else:
                    dp[i][j] = False
        if maxi==0:
            return 1
        return maxi
         

print(Solution().longestPalindrome(s = "abc"))


'''
Problem : https://leetcode.com/problems/longest-palindromic-substring/
Approach :
'''