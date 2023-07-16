import heapq
def dijkstra(V, adj, S):

    dist_arr = [float("inf") for _ in range(V)]
    dist_arr[S] = 0
    heap = [(0,S)]

    while heap:
        dist_upto,node = heapq.heappop(heap)
        
        for i in range(len(adj[node])):
            node_to_go, dist_to_go = adj[node][i]
            total_dist = dist_upto + dist_to_go
            if total_dist<dist_arr[node_to_go]:
                dist_arr[node_to_go] = total_dist
                heapq.heappush(heap,(total_dist, node_to_go))

    return dist_arr

print(dijkstra(3,[[[1,1],[2,6]],[[2,3],[0,1]],[[1,3],[0,6]]],2))