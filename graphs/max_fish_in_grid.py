from typing import List
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        def add_boundaries(row,col):
            #up
            if row-1>=0 and visited[row-1][col]==0 and grid[row-1][col]!=0:
                queue.append((row-1,col))
                visited[row-1][col] = 1
            
            #right
            if col+1<col_len and visited[row][col+1]==0 and grid[row][col+1]!=0:
                queue.append((row,col+1))
                visited[row][col+1] = 1

            #down
            if row+1<row_len and visited[row+1][col]==0 and grid[row+1][col]!=0:
                queue.append((row+1,col))
                visited[row+1][col] = 1

            #left
            if col-1>=0 and visited[row][col-1]==0 and grid[row][col-1]!=0:
                queue.append((row,col-1))
                visited[row][col-1] = 1


        max_fish = 0
        visited = [[0 for _ in range(col_len)] for _ in range(row_len)] 

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c]!=0 and visited[r][c]==0:
                    curr_max = 0
                    queue = [(r,c)]
                    visited[r][c] = 1
                    while queue:
                        curr_row,curr_col = queue.pop(0)
                        curr_max += grid[curr_row][curr_col]
                        visited[curr_row][curr_col] = 1
                        add_boundaries(curr_row,curr_col)
                    max_fish = max(max_fish,curr_max)
        return max_fish
    
'''
Problem : https://leetcode.com/problems/maximum-number-of-fish-in-a-grid
TC - O(m*n)
SC - O(m*n)
Approach :
Simple bfs
while travelling the connected components add the fishes for each and return max
'''