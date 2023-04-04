"""
Problem : https://leetcode.com/problems/spiral-matrix/
"""

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix)
        c = len(matrix[0])
        top = 0
        bottom = r-1
        left = 0
        right = c-1
        sol = []
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                sol.append(matrix[top][i])
            top+=1
            for j in range(top,bottom+1):
                sol.append(matrix[j][right])
            right-=1
            if top<=bottom:
                for k in range(right,left-1,-1):
                    sol.append(matrix[bottom][k])
                bottom-=1
            if left<=right:
                for l in range(bottom,top-1,-1):
                    sol.append(matrix[l][left])
                left+=1
        return sol
    


"""
Approach:
1. Initialize 4 boundary vars to track top, bottom, left and right
2. Repeat this step until top>bottom and left>right
    a. Travel top row from left to right  and increment top
    b. Travel right col from top to bottom and decrement right
    c. check if top<=bottom, if yes, Travel bottom row from right to left and decrement bottom
    d. check if left<=right, if yes, Travel left col from bottom to top and increment left
3. Return

"""