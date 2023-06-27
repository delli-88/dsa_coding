from typing import List

def topologicalOrdering(n: int,edges: List[List[int]]) -> List[int]:
    adj = [[] for _ in range(n+1)]
    for i in range(len(edges)):
        adj[edges[i][0]].append(edges[i][1])

    visited = [0 for _ in range(n+1)]
    sol_stack = []

    for i in range(1,n+1):
        if visited[i]==0:
            dfs(i,adj,visited,sol_stack)
    
    return sol_stack[::-1]

def dfs(node,adj,vis,sol_stack):

    vis[node] =1

    for i in range(len(adj[node])):
        if vis[adj[node][i]]==0:
            dfs(adj[node][i],adj,vis,sol_stack)
    
    sol_stack.append(node)


'''
TC - O(V+E)
SC - O(E)
Approach :
1.Create an adjacency list representation of the graph using the given number of vertices n and edges edges.
2.Initialize a visited array visited of size n+1 with all elements set to 0. This array will keep track of whether a node has been visited during the DFS traversal.
3.Initialize an empty stack sol_stack to store the nodes in topological order.
4.Iterate through all the nodes from 1 to n. For each node i:
    a.If visited[i] is 0, it means the node has not been visited yet. Call the DFS function dfs(i, adj, visited, sol_stack).
5.The dfs function takes a node node, the adjacency list adj, the visited array vis, and the solution stack sol_stack as parameters. It performs the following steps:
    a.Mark node as visited by setting vis[node] to 1.
    b.Iterate through all the adjacent nodes of node in the adjacency list adj[node].
    c.If an adjacent node adj[node][i] has not been visited (vis[adj[node][i]] == 0), recursively call dfs(adj[node][i], adj, vis, sol_stack).
    d.After visiting all the adjacent nodes, add the current node to the sol_stack.
6.Finally, return the reversed sol_stack as the topological ordering of the graph.
'''