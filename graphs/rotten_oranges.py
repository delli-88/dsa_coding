from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid)==1 and len(grid[0])==1:
            if grid[0][0]==1:
                return -1
            return 0
        def rotten_boundaries(row,col):

            max_row, max_col = len(grid)-1, len(grid[row])-1

            if row-1>=0 and (visited_grid[row-1][col]==0):
                visited_grid[row-1][col] = 1
                queue.append((row-1,col))
            if col-1>=0 and visited_grid[row][col-1]==0:
                visited_grid[row][col-1] = 1
                queue.append((row,col-1))
            if row+1<=max_row and visited_grid[row+1][col]==0:
                visited_grid[row+1][col] = 1
                queue.append((row+1,col))
            if col+1<=max_col and visited_grid[row][col+1]==0:
                visited_grid[row][col+1] = 1
                queue.append((row,col+1))
        

        not_rotten = False

        visited_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        queue = deque()
        for r0 in range(len(grid)):
            for c0 in range(len(grid[0])):
                if grid[r0][c0]==2:
                    visited_grid[r0][c0] = 1
                    queue.append((r0,c0))

                if grid[r0][c0]==0:
                    visited_grid[r0][c0] = -1
                if grid[r0][c0]==1:
                    not_rotten = True

        if len(queue)==0:
            if not_rotten:
                return -1
            else:
                return 0

        minutes = -1
        while queue:
            rotten_len = len(queue)
            minutes+=1
            for _ in range(rotten_len):
                curr_rotten_row, curr_rotten_col = queue.popleft()
                rotten_boundaries(curr_rotten_row, curr_rotten_col)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited_grid[i][j]==0:
                    return -1 
        return minutes

'''
Problem : https://leetcode.com/problems/rotting-oranges/
TC - O(4*n*m)-> O(n*m)
SC - O(n*m)
Approach : 
It is a bfs traversal
First we get all rotten oranges and push them into queue, we also maintain a visited array 
if there are no rotten, we then check if we have any fresh oranges, if both are not present return 0 else return -1
Now we follow bfs
we take the queue peek and travel all four boundaries and if they are not rotten and not visited, we rotten them and mark as visited and increment time
We follow until queue is empty
we check if all the fresh oranges rae rotten or not using visited array, if not we return -1
we finally return time counter(minutes)
'''
print(Solution().orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]))
