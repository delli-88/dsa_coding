class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        return self.longestCommonSubsequenceTabSpaceOpt(text1, text2)
        # return self.longestCommonSubsequenceTab(text1,text2)

        # dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        # return self.longestCommonSubsequenceMemoization(len(text1)-1,len(text2)-1,text1,text2,dp)

        # return self.longestCommonSubsequenceRecur(len(text1)-1,len(text2)-1,text1,text2)
    

    # DP Tabulation Space Opt
    def longestCommonSubsequenceTabSpaceOpt(self,text1, text2):
        prev = [0 for _ in range(len(text2)+1)]
        curr = prev[:]

        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j],curr[j-1])
            prev = curr[:]
        return curr[-1]
    '''
    Problem: https://leetcode.com/problems/longest-common-subsequence/description/
    TC - O(n * m)
    SC - O(m)
    Approach for DP Tabulation Space Opt
    1.Create two arrays, prev and curr, initially filled with zeros. These arrays will be used to store the LCS lengths.
    2.Iterate over the characters of text1 and text2 using two nested loops.
    3.Compare the characters at the current positions (i-1, j-1) in text1 and text2. If they are equal, increment the current LCS length by 1 (curr[j] = 1 + prev[j-1]).
    4.If the characters are not equal, take the maximum LCS length from either the previous row (prev[j]) or the current row in the previous column (curr[j-1]).
    5.After each inner loop iteration, update the prev array with the values of the curr array.
    6.Finally, return the last element of the curr array, which represents the length of the LCS.
    '''

    # DP Tabulation
    def longestCommonSubsequenceTab(self,text1, text2):
        prev = [0 for _ in range(len(text2)+1)]
        curr = prev[:]

        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    curr[i][j] = 1 + prev[i-1][j-1]
                else:
                    curr[j] = max(prev[j],curr[j-1])
        return curr[-1]
    '''
    TC - O(n * m)
    SC - O(n * m)
    Approach for DP Tabulation:
    1.Create a 2D array dp of size (len(text1)+1) x (len(text2)+1) to store the lengths of LCS for different subproblems. Initialize all elements of dp to 0.
    2.Iterate through the rows and columns of dp using two nested loops, starting from index 1.
    3.For each cell dp[i][j], compare the characters text1[i-1] and text2[j-1] (since the strings are 0-indexed).
        a.If the characters are the same, set dp[i][j] to 1 plus the value of the LCS length for the previous characters: dp[i-1][j-1].
        b.If the characters are different, set dp[i][j] to the maximum value between the LCS length when either text1[i-1] or text2[j-1] is excluded: max(dp[i-1][j], dp[i][j-1]).
    4.After iterating through all cells, the value at dp[-1][-1] represents the length of the LCS for the entire strings text1 and text2. Return this value.
    '''

    # DP Memoization
    def longestCommonSubsequenceMemoization(self,ind1,ind2,str1,str2,dp):
        if ind1<0 or ind2<0:
            return 0
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]

        if str1[ind1]==str2[ind2]:
            dp[ind1][ind2] = 1 + self.longestCommonSubsequenceMemoization(ind1-1,ind2-1,str1,str2,dp)
            return dp[ind1][ind2]
        
        dp[ind1][ind2] = max(self.longestCommonSubsequenceMemoization(ind1,ind2-1,str1,str2,dp),self.longestCommonSubsequenceMemoization(ind1-1,ind2,str1,str2,dp))
        return dp[ind1][ind2]
    
    '''
    TC - O(n * m)
    SC - O(n * m) + O(n + m)
    Approach for DP Memoization:
    1.If either ind1 or ind2 becomes negative, it means we have reached the end of one of the strings, so the length of the LCS is 0. Return 0 in this case.
    2.If the characters at the current indices ind1 and ind2 are the same, increment the LCS length by 1 and recursively call the function with the updated indices ind1-1 and ind2-1, moving to the previous characters of both strings.
    3.If the characters at the current indices are different, recursively call the function with either ind1 decremented (moving to the previous character in str1) or ind2 decremented (moving to the previous character in str2), and take the maximum of the two recursive calls.
    4.Return the maximum LCS length obtained from step 3.
    '''
    
    # Recursion
    def longestCommonSubsequenceRecur(self,ind1,ind2,str1,str2):
        if ind1<0 or ind2<0:
            return 0
        
        if str1[ind1]==str2[ind2]:
            return 1 + self.longestCommonSubsequenceRecur(ind1-1,ind2-1,str1,str2)
        
        return max(self.longestCommonSubsequenceRecur(ind1,ind2-1,str1,str2),self.longestCommonSubsequenceRecur(ind1-1,ind2,str1,str2))
    
    '''
    Approach for DP Recursion:
    1.If either ind1 or ind2 is less than 0, return 0 as the base case.
    2.Check if the characters at indices ind1 and ind2 in str1 and str2 are equal.
        a.If they are equal, increment the result by 1 and make a recursive call to longestCommonSubsequenceRecur with ind1-1, ind2-1, str1, and str2.
    3.If the characters at indices ind1 and ind2 are not equal, make two recursive calls:
        a.One with ind1, ind2-1, str1, and str2, representing skipping the character at ind1 in str1.
        b.Another with ind1-1, ind2, str1, and str2, representing skipping the character at ind2 in str2.
    4.Return the maximum value between the two recursive calls from step 3.
    5.The result will be the length of the longest common subsequence between str1 and str2.
    '''

    
print(Solution().longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))
