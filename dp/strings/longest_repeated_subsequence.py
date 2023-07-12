def longestRepeatedSubsequence(s: str) -> int:

    dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]

    for i in range(1, len(s)+1):
        for j in range(1, len(s)+1):
            if s[i-1]==s[j-1] and i!=j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

print(longestRepeatedSubsequence('abacbc'))

'''
approach : 
1.Create a 2D array dp of size (len(s) + 1) x (len(s) + 1). This array will store the lengths of the longest repeated subsequences for different prefixes of the input string s.
2.Initialize the first row and the first column of dp with zeros, as there are no repeated subsequences when the prefix or suffix has length zero.
3.Iterate over the indices i and j from 1 to len(s), representing the lengths of prefixes s[:i] and s[:j], respectively.
4.Check if the characters at indices i-1 and j-1 in s are equal, indicating a potential repeated subsequence. Additionally, ensure that i is not equal to j to avoid counting the same character as a repetition.
5.If the characters are equal and i is not equal to j, set dp[i][j] to 1 plus the value of dp[i-1][j-1]. This means the length of the longest repeated subsequence for the prefixes s[:i] and s[:j] is one more than the length of the longest repeated subsequence for the prefixes s[:i-1] and s[:j-1].
6.If the characters are not equal or i is equal to j, set dp[i][j] to the maximum of dp[i-1][j] and dp[i][j-1]. This means the length of the longest repeated subsequence for the prefixes s[:i] and s[:j] is the maximum of the lengths of the longest repeated subsequences for the prefixes s[:i-1] and s[:j], and s[:i] and s[:j-1], respectively.
7.Finally, return dp[-1][-1], which represents the length of the longest repeated subsequence for the entire input string s.
'''