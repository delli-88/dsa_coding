from typing import List
def cycleDirectedGraph(n: int, edges: List[List[int]]) -> bool:
    adj = [[] for _ in range(n+1)]
    for i in range(len(edges)):
        adj[edges[i][0]].append(edges[i][1])
    
    back_track = [0 for _ in range(n+1)] 
    vis = [False for _ in range(n+1)]
    for i in range(1,n+1):
        if vis[i]==False:
            if cyclePresent(i,adj,vis, back_track):
                return 1
    return 0

def  cyclePresent(node,adj,vis,back_track):
    vis[node] = True
    back_track[node] = True
    for i in range(len(adj[node])):
        if vis[adj[node][i]]==False:
            if cyclePresent(adj[node][i], adj, vis, back_track):
                return True
        elif back_track[adj[node][i]]==True:
            return True

    back_track[node] = False
    return False

'''
Approach :
1.Create an adjacency list representation of the graph. For each vertex, store a list of its adjacent vertices.
2.Initialize two arrays: vis and back_track. Both arrays are of size n+1, where n is the number of vertices in the graph. Initialize all elements in both arrays to False.
3.Iterate through each vertex from 1 to n and perform the following steps:
    a.If the vertex has not been visited (vis[i] is False), call the cyclePresent function to check if a cycle is present starting from that vertex.
    b.If a cycle is found (cyclePresent returns True), return True immediately as there is a cycle in the graph.
4.If no cycles are found after checking all vertices, return False.
5.The cyclePresent function is a recursive function that performs a DFS starting from a given vertex. It takes the current vertex, the adjacency list, the visited array, and the backtracking array as inputs.
6.Mark the current vertex as visited by setting vis[node] and back_track[node] to True.
7.Iterate through each adjacent vertex of the current vertex:
    a.If the adjacent vertex has not been visited, recursively call cyclePresent on the adjacent vertex.
    b.If cyclePresent returns True, it means a cycle has been found, so return True immediately.
    c.If the adjacent vertex has been visited and is currently in the backtracking process (i.e., back_track[adj[node][i]] is True), it indicates the presence of a cycle, so return True.
8.After exploring all adjacent vertices, mark the current vertex as not part of the backtracking process by setting back_track[node] to False.
9.If no cycles are found after checking all adjacent vertices, return False.
'''