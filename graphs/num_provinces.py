from typing import List
class Solution:
    def dfs(self,node,vis,adj):
        vis[node] = 1

        for i in range(len(adj[node])):
            if vis[adj[node][i]]==0:
                self.dfs(adj[node][i],vis,adj)  
        return
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        n = len(isConnected)
        provinces = 0
        visited = [0]*(n+1)
        adj_map = {}

        # creating adjacency List
        for i in range(1,n+1):
            for j in range(1,n+1):
                if isConnected[i-1][j-1]==1:
                    if adj_map.get(i): 
                        adj_map[i].append(j)
                    else:
                        adj_map[i] = [j]
        
        #calc provinces
        for i in range(1,n+1):
            if visited[i]==0:
                provinces+=1
                self.dfs(i,visited,adj_map)
        return provinces
    

'''
Problem : https://leetcode.com/problems/number-of-provinces/
TC -  O(N) + O(V+2E)
SC - O(N)
Approach:
We need a visited array initialized to 0 of len n+1, representing the nodes that are not visited.
Run the for loop looping from 1 to N+1, and call the DFS if the node is not visited
DFS function call will make sure that it starts the DFS call from that unvisited node, and visits all the nodes that are in that province, and at the same time, it will also mark them as visited. 
Since the nodes traveled in a traversal will be marked as visited, they will no further be called for any further DFS traversal. 
Keep repeating these steps, for every node that you find unvisited, and visit the entire province. 
Add a counter variable to count the number of times the DFS function is called, as in this way we can count the total number of starting nodes, which will give us the number of provinces.
return provinces
'''