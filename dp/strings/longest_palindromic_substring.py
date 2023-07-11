class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        return self.longestPalindromeRecursive(s, 0, len(s)-1, dp)
    
    def longestPalindromeRecursive(self, s, idx1, idx2, dp):
        if idx1>idx2:
            return 0
        
        if idx1==idx2:
            return 1
        
        if dp[idx1][idx2]!=-1:
            return dp[idx1][idx2]
        
        if s[idx1]==s[idx2]:
            return 2+ self.longestPalindromeRecursive(s, idx1+1, idx2-1, dp)
        
        opt1 = self.longestPalindromeRecursive(s, idx1+1, idx2, dp)
        opt2 = self.longestPalindromeRecursive(s, idx1, idx2-1, dp)

        dp[idx1][idx2] = max(opt1, opt2)
        return dp[idx1][idx2]


print(Solution().longestPalindrome(s = "abeedba"))


'''
Problem : https://leetcode.com/problems/longest-palindromic-substring/
Approach :
'''