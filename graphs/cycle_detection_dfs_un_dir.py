from typing import List
class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [0]*V
        for i in range(V):
            if visited[i]==0:
                if self.cycleDetect(i,-1,visited,adj):
                    return True
        
        return False

    def cycleDetect(self, node, parent, visited, adj):

        visited[node]=1

        for i in range(len(adj[node])):
            if visited[adj[node][i]]==0:
                if self.cycleDetect( adj[node][i], node, visited, adj):
                    return True
            elif parent!=adj[node][i]:
                return True
        
        return False

print(Solution().isCycle(5,[[1],[2,0,4],[1,3],[2,4],[1,3]]))
# print(Solution().isCycle(5,[[1],[2],[3],[4],[]]))






'''
Problem : https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
TC - O(V+E)
SC - O(V)
Approach :

1.Initialize a visited array of size V to keep track of visited vertices. Set all elements to 0 initially.
2.Iterate through each vertex i from 0 to V-1. (for non-connected components if any)
3.If the vertex i is not visited, call the cycleDetect function with arguments i, -1 (indicating no parent), visited, and adj.
4.In the cycleDetect function:
    4a.Mark the current node as visited by setting visited[node] to 1.
    4b.Iterate through each neighbor of the current node using the adjacency list adj[node].
    4c.If the neighbor vertex is not visited, recursively call the cycleDetect function with arguments adj[node][i] (neighbor vertex), node (current node as the parent), visited, and adj.
    4d.If the neighbor vertex is already visited and it is not the parent of the current node, it indicates the presence of a cycle. Return True.
5.If no cycle is detected in the graph, return False.
'''