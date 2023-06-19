import sys


def nQueens(n: int) -> str:
    board = [[0 for _ in range(n)] for _ in range(n)]
    sol = nQueensHelper(n,0,0,0,[],board)
    for k in range(len(sol)):
        for i in range(n):
            for j in range(n):
                print(sol[k][i][j], end="")
            print()
        print()
    return sol

def nQueensHelper(n,r,c,q,sol,board):
    if r>=n:
        if q==n:
            sol.append([[i for i in board[j]] for j in range(n)])
        return sol
    
    if c>=n:
        nQueensHelper(n,r+1,0,q,sol,board)
    else:
        if queenCheck(n,r,c,board):
            board[r][c]=1
            nQueensHelper(n,r,c+1,q+1,sol,board)
            board[r][c]=0

            nQueensHelper(n,r,c+1,q,sol,board)

        else:
            nQueensHelper(n,r,c+1,q,sol,board)

    return sol


def queenCheck(n,r,c,board):
    if board[r][c]==1:
        return False
    
    for i in range(n):
        if board[r][i]==1:
            return False
    
    for i in range(n):
        if board[i][c]==1:
            return False
    
    #top-left
    i=r
    j=c
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    
    #top-right
    i=r
    j=c
    while i>=0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j+=1

    #bottom-left
    i=r
    j=c
    while i<n and j>=0:
        if board[i][j]==1:
            return False
        i+=1
        j-=1

    #bottom-right
    i=r
    j=c
    while i<n and j<n:
        if board[i][j]==1:
            return False
        i+=1
        j+=1

    return True



def main():
    n = int(input())
    result = nQueens(n)
    # print(result)

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    main()

'''
Approach :
1.Create a 2D board of size n x n, initialized with zeros, to represent the chessboard.
2.Define a function nQueensHelper that takes the following parameters:
    n: the size of the board
    r: the current row
    c: the current column
    q: the number of queens placed so far
    sol: a list to store the solutions
    board: the 2D board
3.In the nQueensHelper function:
    Base case:
        If r is equal to or greater than n, check if q is equal to n. If it is, append a copy of the board to the sol list as a valid solution.
        Return the sol list.
    a.If c is equal to or greater than n, move to the next row (r+1) and start from the first column (c=0) recursively by calling nQueensHelper.
    b.If the current position (r, c) is safe to place a queen, i.e., the queenCheck function returns True:
        i.Set board[r][c] to 1 to indicate a queen is placed at this position.
        ii.Recursively call nQueensHelper with the next column (c+1), the number of queens increased by 1 (q+1), and the updated board.
        iii.Set board[r][c] back to 0 to backtrack and explore other possibilities.
    c.Recursively call nQueensHelper with the next column (c+1), the same number of queens (q), and the current board (board).
    d.Return the sol list.
4.Initialize the sol list as an empty list.
5.Call the nQueensHelper function with the board size n=4 (or any other desired value), starting from the first row (r=0), the first column (c=0), the number of queens placed (q=0), the sol list, and the empty board.
6.If the sol list is empty, print "No Solution Exists".
7.Iterate through each solution in the sol list:
    Print the board configuration row by row.
8.Return the sol list.
'''