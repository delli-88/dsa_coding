# incomplete code

from typing import List
class Solution:

    def get_adjacency_list(self, edges):
        
        adjacency_list = {}
        for i in range(len(edges)):
            if adjacency_list.get(edges[i][0]):
                adjacency_list[edges[i][0]].append(edges[i][1])
            else:
                adjacency_list[edges[i][0]] = [edges[i][1]]

            if adjacency_list.get(edges[i][1]):
                adjacency_list[edges[i][1]].append(edges[i][0])
            else:
                adjacency_list[edges[i][1]] = [edges[i][0]]

        return adjacency_list
    
    def dfs_vertices_count(self, adj, vis, v, count):
        vis[v] = 1
        if adj.get(v):
            for i in range(len(adj[v])):
                if vis[adj[v][i]]==-1:
                    count[0]+=1
                    self.dfs_vertices_count(adj, vis, adj[v][i],count)
        
        return count



    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list = self.get_adjacency_list(edges)
        visited = [-1 for _ in range(n+1)]

        for i in range(n):
            if visited[i]==-1:
                node_count = self.dfs_vertices_count(adjacency_list, visited, 5,[1])[0]
                for j in range(node_count):


        print(visited,node_count)





print(Solution().countCompleteComponents(6,edges = [[0,1],[0,2],[1,2],[3,4]]))