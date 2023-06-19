from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_board = {}
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    curr_row = f'R{i}{board[i][j]}'
                    curr_col = f'C{j}{board[i][j]}'
                    curr_box = f'B{(i//3)*3 + (j//3)}{board[i][j]}'

                    if hash_board.get(curr_row) or hash_board.get(curr_col) or hash_board.get(curr_box):
                        return False
                    hash_board[curr_row] = True
                    hash_board[curr_col] = True
                    hash_board[curr_box] = True
        return True

'''
Approach : 
1.Create an empty hash table (dictionary) hash_board to store the presence of each digit in each row, column, and 3x3 box.
2.Iterate over each cell of the Sudoku board using two nested loops.
3.For each non-empty cell (cell value is not '.'), do the following:
    a.Create three keys curr_row, curr_col, and curr_box to represent the current digit's presence in the respective row, column, and 3x3 box.
        i.curr_row is formed by concatenating 'R' with the row index i and the digit value board[i][j].
        ii.curr_col is formed by concatenating 'C' with the column index j and the digit value board[i][j].
        iii.curr_box is formed by concatenating 'B' with the box index (i//3)*3 + (j//3) and the digit value board[i][j].
    b.Check if any of the keys curr_row, curr_col, or curr_box already exist in the hash_board dictionary. If any key exists, it means the current digit is already present in either the same row, column, or 3x3 box, violating the Sudoku rules. In this case, return False.
    c.If none of the keys exist in the hash_board dictionary, it is a valid occurrence of the digit. Add all three keys to the hash_board dictionary and set their values to True.
4.If the iteration completes without returning False, it means the Sudoku board is valid. Return True.
'''


print(Solution().isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))