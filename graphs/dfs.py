def dfs(starting_node, graph_adjacency_list):
    vis = [0]*(len(graph_adjacency_list)+1)
    return dfs_helper(starting_node,graph_adjacency_list,[],vis)

def dfs_helper(node,adj,dfs,vis):
    # if vis[node]==1:
    #     return dfs

    vis[node] = 1
    dfs.append(node)

    for i in range(len(adj[node])):
        if vis[adj[node][i]]==0:
            dfs_helper(adj[node][i],adj,dfs,vis)
    
    return dfs

