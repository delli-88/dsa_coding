class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        return self.minDistanceTabSpaceOpt(word1, word2)

        # dp = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]
        # return self.minDistanceRecursiveMemo(word1,word2,len(word1)-1,len(word2)-1, dp)

    def minDistanceTabSpaceOpt(self, word1, word2):
        prev = [0 for _ in range(len(word2)+1)]
    
        for i in range(len(word2)+1):
            prev[i] = i
        
        curr = prev[:]
        
        for idx1 in range(1, len(word1)+1):
            curr[0] = idx1
            for idx2 in range(1, len(word2)+1):
                if word1[idx1-1]==word2[idx2-1]:
                    curr[idx2] = prev[idx2-1]
                else:

                    insert = curr[idx2-1]
                    delete = prev[idx2]
                    replace = prev[idx2-1]

                    curr[idx2] = 1 + min(insert, delete, replace)
            
            prev = curr[:]
        return curr[-1]


    def minDistanceTab(self, word1, word2):
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for i in range(len(word2)+1):
            dp[0][i] = i

        for i in range(len(word1)+1):
            dp[i][0] = i
        
        for idx1 in range(1, len(word1)+1):
            for idx2 in range(1, len(word2)+1):
                if word1[idx1-1]==word2[idx2-1]:
                    dp[idx1][idx2] = dp[idx1-1][idx2-1]
                else:

                    insert = dp[idx1][idx2-1]
                    delete = dp[idx1-1][idx2]
                    replace = dp[idx1-1][idx2-1]

                    dp[idx1][idx2] = 1 + min(insert, delete, replace)
        
        return dp[-1][-1]

    def minDistanceRecursiveMemo(self, word1,word2,idx1, idx2, dp):

        if idx1<0:
            return idx2+1

        if idx2<0:
            return idx1+1
        
        if dp[idx1][idx2]!=-1:
            return dp[idx1][idx2]
        
        if word1[idx1]==word2[idx2]:
            dp[idx1][idx2] = self.minDistanceRecursive(word1, word2, idx1-1, idx2-1, dp) 
        else:

            insert = self.minDistanceRecursive(word1, word2, idx1, idx2-1, dp)
            delete = self.minDistanceRecursive(word1, word2, idx1-1, idx2, dp)
            replace = self.minDistanceRecursive(word1, word2, idx1-1, idx2-1, dp)

            dp[idx1][idx2] = 1 + min(insert, delete, replace)
        return dp[idx1][idx2]

    


print(Solution().minDistance(word1 = "", word2 = "ros"))


'''
Approach :
1.Create a 2D dynamic programming table dp with dimensions (len(word1)+1) x (len(word2)+1) and initialize all values to 0.
2.Set the base cases: For each index i from 0 to the length of word2, set dp[0][i] = i to represent the minimum number of operations required to convert an empty string to word2[:i].
3.Similarly, for each index i from 0 to the length of word1, set dp[i][0] = i to represent the minimum number of operations required to convert word1[:i] to an empty string.
4.Iterate over each index idx1 from 1 to the length of word1 (inclusive).
5.Within the outer loop, iterate over each index idx2 from 1 to the length of word2 (inclusive).
6.Check if the characters at word1[idx1-1] and word2[idx2-1] are equal. If they are equal, assign dp[idx1][idx2] = dp[idx1-1][idx2-1] because no operation is required to match the characters.
7.If the characters are not equal, calculate three possible operations: insert, delete, and replace.
    i.insert: Assign dp[idx1][idx2-1] as the minimum number of operations to convert word1[:idx1] to word2[:idx2-1] plus one additional insert operation.
    ii.delete: Assign dp[idx1-1][idx2] as the minimum number of operations to convert word1[:idx1-1] to word2[:idx2] plus one additional delete operation.
    iii.replace: Assign dp[idx1-1][idx2-1] as the minimum number of operations to convert word1[:idx1-1] to word2[:idx2-1] plus one additional replace operation.
    a.Set dp[idx1][idx2] to the minimum of the above three values.
8.After completing the iteration, the value at dp[-1][-1] represents the minimum number of operations required to convert word1 to word2. Return this value as the result.
'''