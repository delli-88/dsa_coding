from typing import List

# Outputs a List[] 
def bfs(V: int, adj: List[List[int]]) -> List[int]:
    queue = [0]
    bfs = []
    vis = [0]*V
    while queue:
        queue_first = queue.pop(0)
        if vis[queue_first]==0:
            vis[queue_first] = 1
            bfs.append(queue_first)
        for i in adj[queue_first]:
            if vis[i]==0:
                queue.append(i)
    return bfs

# Outputs a List[List[]] includes the levels
def bfs(starting_node, graph_adjacency_list) -> List[List]:
    queue = [starting_node]
    bfs = [[starting_node]]
    visited = [0]* (len(graph_adjacency_list)+1)
    visited[starting_node] = 1
    while queue:
        queue_len = len(queue)
        for _ in range(queue_len):
            popped = queue.pop(0)
            for i in range(len(graph_adjacency_list[popped])):
                if visited[graph_adjacency_list[popped][i]]==0:
                    queue.append(graph_adjacency_list[popped][i])
                    visited[graph_adjacency_list[popped][i]] = 1
        if queue:
            bfs.append(queue[:])
    return bfs