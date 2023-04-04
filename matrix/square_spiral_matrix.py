"""
Problem Description
Given an integer A, generate a square matrix filled with elements from 1 to A*A in spiral order. The spiral order will be clockwise in nature starting from (0,0)

Input format
One line of input, containing a single integer A.

Output format
Print a 2-d matrix of size A x A satisfying the spiral order.

Sample Input 1
3

Sample Output 1
1 2 3
8 9 4
7 6 5
"""

from typing import List

def spiralMatrixII(n: int) -> List[List[int]]:
    top_row = 0
    bottom_row = n-1
    left_col = 0
    right_col = n-1
    arr = []
    for r in range(n):
        arr.append([0 for _ in range(n)])
    count = 1
    while count<=(n*n):
        for t in range(left_col,right_col+1):
            arr[top_row][t] = count
            count+=1
        top_row+=1
        for r in range(top_row,bottom_row+1):
            arr[r][right_col] = count
            count+=1
        right_col-=1
        for b in range(right_col,left_col-1,-1):
            arr[bottom_row][b] = count
            count+=1
        bottom_row-=1
        for l in range(bottom_row,top_row-1,-1):
            arr[l][left_col] = count
            count+=1
        left_col+=1

    return arr


def main():
    n = int(input())
    matrix = spiralMatrixII(n)
    for row in matrix:
        print(*row)

if __name__=="__main__":
    main()