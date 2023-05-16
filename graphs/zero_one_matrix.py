from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        sol = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        vis = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        queue = []
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c]==0:
                    queue.append((r,c,0))
        while queue:
            curr_row, curr_col, curr_dis = queue.pop(0)
            if vis[curr_row][curr_col]==0:
                sol[curr_row][curr_col] = curr_dis
                vis[curr_row][curr_col] = 1
            self.travel_boundaries(curr_row,curr_col,curr_dis,mat,vis,queue)
            
        return sol
    
    
    def travel_boundaries(self,r,c,d,mat,vis,queue):
        max_row = len(mat)
        max_col = len(mat[0])
        row_dirs = [-1,0,1,0]
        col_dirs = [0,1,0,-1]
        for i in range(4):
            if r+row_dirs[i]>=0 and r+row_dirs[i]<max_row and c+col_dirs[i]>=0 and c+col_dirs[i]<max_col and vis[r+row_dirs[i]][c+col_dirs[i]]==0:
                queue.append((r+row_dirs[i],c+col_dirs[i],d+1))
        return 

'''
Problem : https://leetcode.com/problems/01-matrix
TC - O(n*m)
SC - O(n*m)
Approach :
First we take all zeros into our queue
and while the queue is empty we do below steps
    we take the front element and if it is not already visited, we visit that and update the sol array with its distance
    and we travel all 4 directions and append those in a queue which are not visited by incrementing the dist by 1
return sol
'''
print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))

