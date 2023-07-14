import heapq
class Solution:
    def primsAlgo(self, v, adj_list):
        visited = [0 for _ in range(v)]
        heap = []
        heapq.heappush(heap, (0,0)) #(edge_weight, curr_node) 
        min_cost = 0   

        while heap:
            edge_weight, curr_node = heapq.heappop(heap)
            if visited[curr_node]==0:
                visited[curr_node] = 1
                min_cost+=edge_weight

                for i in range(len(adj_list[curr_node])):
                    if visited[adj_list[curr_node][i][0]]==0:
                        heapq.heappush(heap,(adj_list[curr_node][i][1],adj_list[curr_node][i][0]))
        return min_cost
    
    def spanningTree(self, V, adj):
        adj_list = [[] for _ in range(V)]

        for i in range(len(adj)):
            adj_list[adj[i][0]].append((adj[i][1],adj[i][2]))
            adj_list[adj[i][1]].append((adj[i][0],adj[i][2]))
        
        return self.primsAlgo(V, adj_list)
        
    
    
print(Solution().spanningTree(5,[[0,1,5],[1,2,3],[0,2,1]]))

'''
Approach :
1.Create a visited array to track which vertices have been visited during the algorithm.
2.Create a heap data structure to store the edges of the graph.
3.Initialize the heap with the first vertex (0) and assign a weight of 0.
4.Initialize the minimum cost to 0.
5.While the heap is not empty:
    a.Pop the edge with the minimum weight from the heap.
    b.If the current vertex has not been visited:
        i.Mark the current vertex as visited.
        ii.Add the edge weight to the minimum cost.
        iii.Iterate through the adjacent vertices of the current vertex and push them into the heap.
6.Return the minimum cost.
'''