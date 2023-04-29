from typing import List

# dfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        init_color = image[sr][sc]
        if init_color==color:
            return image
        visited = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
        return self.fill_boundary(image,sr,sc,init_color,color,visited)

    def fill_boundary_dfs(self,image,r,c,init_color,new_color,visitid):
        max_row = len(image)
        max_col = len(image[0])
        row = [-1,0,1,0]
        col = [0,1,0,-1]
        if visitid[r][c]==0 and image[r][c]==init_color:
            image[r][c] = new_color
            for f in range(4):
                c_row = r+row[f]
                c_col = c+col[f]
                if c_row>=0  and c_col<max_col and c_row<max_row and c_col>=0:
                    self.fill_boundary_dfs(image,c_row,c_col,init_color,new_color,visitid)
        return image
'''
Problem : https://leetcode.com/problems/flood-fill
TC - O(m*n)
SC - O(m*n)
Approach :
We follow dfs here
at every pixel, we color it to new and travel the boundaries(u-r-d-l) only if the pixels are within boundaries
and we follow dfs recursion
and return image
'''


'''
# bfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        
        def fill_boundary(r,c):
            max_row = len(image)
            max_col = len(image[0])
            row = [-1,0,1,0]
            col = [0,1,0,-1]

            for f in range(4):
                c_row = r+row[f]
                c_col = c+col[f]
                if c_row>=0  and c_col<max_col and c_row<max_row and c_col>=0 and image[c_row][c_col]==flood_color and visited[c_row][c_col]==0:
                    queue.append((c_row,c_col))
            # # up
            # if r-1>=0 and image[r-1][c]==flood_color and visited[r-1][c]==0:
            #     queue.append((r-1,c))

            # # right
            # if c+1<max_col and image[r][c+1]==flood_color and visited[r][c+1]==0:
            #     queue.append((r,c+1))

            # # down
            # if r+1<max_row and image[r+1][c]==flood_color and visited[r+1][c]==0:
            #     queue.append((r+1,c))
            
            # # left
            # if c-1>=0 and image[r][c-1]==flood_color and visited[r][c-1]==0:
            #     queue.append((r,c-1))


        queue = [(sr,sc)]
        visited = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
        flood_color = image[sr][sc]
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                curr_row,curr_col = queue.pop(0)
                image[curr_row][curr_col] = color
                visited[curr_row][curr_col] = 1
                fill_boundary(curr_row,curr_col)
        return image
'''

            


        



print(Solution().floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))