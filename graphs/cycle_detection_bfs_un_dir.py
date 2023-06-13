from typing import List
from collections import deque

class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [0]*V

        for i in range(V):
            if visited[i]==0:
                if self.detectCycle(i, adj, visited):
                    return True
        return False


    def detectCycle(self, start, adj, visited):
        
        queue = deque()
        queue.append((start,-1))

        while queue:
            queue_front, parent = queue.popleft()
            visited[queue_front] = 1
            cur_adj_len = len(adj[queue_front])
            for i in range(cur_adj_len):
                if parent!=adj[queue_front][i]:
                    if visited[adj[queue_front][i]]==1:
                        return True
                    queue.append((adj[queue_front][i],queue_front))
        return False



#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends


'''
Problem : https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
TC - O(V+E)
SC - O(V)
Approach :
1.We start by initializing a visited array of size V (number of vertices) to keep track of visited nodes. All nodes are initially marked as unvisited (0).
2.We iterate over all the vertices of the graph using a for loop.
3.For each unvisited vertex, we call the detectCycle function with the vertex index, adjacency list, and the visited array.
4.In the detectCycle function, we start a BFS traversal from the given vertex. We use a queue to store the vertices to be visited.
5.We enqueue the starting vertex along with a parent marker (-1) into the queue.
6.While the queue is not empty, we dequeue a vertex from the front of the queue.
7.We mark the dequeued vertex as visited (set visited[queue_front] = 1).
8.We iterate over the adjacency list of the dequeued vertex to explore its neighbors.
9.If the neighbor is not the parent of the dequeued vertex (to avoid considering the edge that leads back to the parent as a cycle), we check if it is already visited (visited[adj[queue_front][i]] == 1). If it is visited, it means there is a cycle in the graph, and we return True.
10.If the neighbor is not visited, we mark it as visited (visited[adj[queue_front][i]] = 1) and enqueue it into the queue along with the current vertex as the parent.
11.If we have traversed all the vertices without finding a cycle, we return False from the detectCycle function.
12.Finally, if we have checked all the vertices and found no cycles, we return False from the isCycle function. Otherwise, we return True if a cycle is detected during the traversal.
'''