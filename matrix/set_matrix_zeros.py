from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_first_row_zero = False
        is_first_col_zero = False
        is_first_row_col_zero = False

        row_len = len(matrix)
        col_len = len(matrix[0])
        for r1 in range(row_len):
            for c1 in range(col_len):
                if r1==0 and c1==0 and matrix[r1][c1]==0:
                    is_first_row_col_zero = True
                elif r1==0 and matrix[r1][c1]==0:
                    is_first_row_zero = True
                elif c1==0 and matrix[r1][c1]==0:
                    is_first_col_zero = True
                else:
                    if matrix[r1][c1]==0:
                        matrix[r1][0] = 0
                        matrix[0][c1] = 0
        
        for r2 in range(1,row_len):
            for c2 in range(1,col_len):
                if matrix[r2][0]==0 or matrix[0][c2]==0:
                    matrix[r2][c2] = 0

        if is_first_col_zero or is_first_row_col_zero:
            for r in range(row_len):
                matrix[r][0] = 0
        
        if is_first_row_zero or is_first_row_col_zero:
            for c in range(col_len):
                matrix[0][c] = 0
        
        return matrix

        """
        TC - O(N*M)
        SC - O(1)
        Approach:
        Initialize three vars to track if we need to set first row, first col to zeros ornot
        Travel the matrix once and check
            if any of element in first row is zero we set 'is_first_row_zero' to zero
            if any of element in first col is zero we set 'is_first_col_zero' to zero
            if any of both of first row & first col we set 'is_first_row_col_zero' to zero
            if we are not at either first row or first col:
                we check if the curr ele is zero and we mark the zero row curr col and curr row zero col as '0' for reference
            
        we travel the matrix again from second row and second col and 
            check if either zero row curr col or  curr row zero col is '0', 
            if yes then mark the curr ele as zero

        Travel first row, 
            if  is_first_row_zero is 0 or is_first_row_col_zero, update entire row to 0

        Travel first col, 
            if  is_first_col_zero is 0 or is_first_row_col_zero, update entire col to 0
        
        return matrix

        """