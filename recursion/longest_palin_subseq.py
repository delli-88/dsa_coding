class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        maxi = [0]
        self.longestPalindromeSubseqHelper(s, [], 0, maxi)
        return maxi[0]

    def longestPalindromeSubseqHelper(self, s, out, pos, maxi):
        if pos>=len(s):
            if self.is_polindeome(out):
                maxi[0] = max(maxi[0], len(out))
            return maxi

        out.append(s[pos])
        self.longestPalindromeSubseqHelper(s, out, pos+1, maxi)
        out.pop()

        self.longestPalindromeSubseqHelper(s, out, pos+1, maxi)

        return maxi

    def is_polindeome(self,arr):
        if len(arr)<=1:
            return True
        start = 0
        end = len(arr)-1
        while start<end:
            if arr[start]!=arr[end]:
                return False
            start+=1
            end-=1
        return True

'''
Problem : https://leetcode.com/problems/longest-palindromic-subsequence/
Approach : It will give TLE
Same as finding subsequences,
If pos reaches len, then check if the output is a palindrome and if yes check and update the maxi
'''