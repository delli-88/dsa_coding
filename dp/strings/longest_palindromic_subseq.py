class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.longestPalindromeTab(s)
        # dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        # return self.longestPalindromeRecursive(s, 0, len(s)-1, dp)
    
    def longestPalindromeTab(self,s):
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        for idx1 in range(len(s)-1,-1,-1):
            for idx2 in range(idx1+1,len(s)):
                if s[idx1]==s[idx2]:
                    dp[idx1][idx2] =  2+ dp[idx1+1][idx2-1] 
                else:
                    opt1 = dp[idx1+1][idx2]
                    opt2 = dp[idx1][idx2-1]

                    dp[idx1][idx2] = max(opt1, opt2)  

        return dp[0][-1]
    
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
Problem : https://leetcode.com/problems/longest-palindromic-subsequence/
Approach :
1.Create a 2D array dp with dimensions (len(s) x len(s)) and initialize all elements to 0.
2.Iterate over the string s and set dp[i][i] to 1 for all characters in s. This represents the base case where each individual character is a palindrome of length 1.
3.Iterate in reverse order from the last index idx1 of s to the first index, and for each idx1, iterate from idx1 + 1 to the last index idx2.
4.If the characters s[idx1] and s[idx2] are equal, set dp[idx1][idx2] to 2 + dp[idx1 + 1][idx2 - 1]. This represents the case where the current characters form a palindrome and the length is increased by 2 compared to the inner substring.
5.If the characters s[idx1] and s[idx2] are not equal, set dp[idx1][idx2] to the maximum value between dp[idx1 + 1][idx2] and dp[idx1][idx2 - 1]. This represents the case where we skip one of the characters and find the maximum length palindrome in the remaining substring.
6.Finally, return dp[0][-1], which represents the length of the longest palindrome in the entire string s.
'''