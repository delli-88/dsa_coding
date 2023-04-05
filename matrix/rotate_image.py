from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # Transpose
        matrix_len = len(matrix)
        for r in range(matrix_len):
            for c in range(matrix_len):
                if r<c:
                    matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]
        
        # Reverse
        for row in range(matrix_len):
            ptr1 = 0
            ptr2 = matrix_len-1

            while ptr1<ptr2:
                matrix[row][ptr1],matrix[row][ptr2] = matrix[row][ptr2],matrix[row][ptr1]
                ptr1+=1
                ptr2-=1
        
        return matrix


    """
    Problem:https://leetcode.com/problems/rotate-image/
    TC - O(n^2)
    SC - O(1)
    Approach:
    We can rotate the given matrix in two steps
        1. Do Transpose of the given matrix
        2. Reverse each row  
    """ 

    """
    #Brute Force
    sol = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    mat_len = len(matrix)-1
    for i in range(len((matrix))):
        for j in range(len(matrix[0])):
            # matrix[i][j],matrix[j][mat_len-i] = mat_len[j][mat_len-i],matrix[i][j]
            sol[j][mat_len-i] = matrix[i][j]
    return sol
    """

print(Solution().rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))