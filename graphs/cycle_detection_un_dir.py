from typing import List
class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:

        vis = [0 for _ in range(V)]
        hash_map = {}

        cycle_found = False

        for i in range(V):
            if vis[i]==0:
                vis[i] = 0
                queue = [i]
                while queue and cycle_found==False:
                    queue_len = len(queue)
                    for _ in range(queue_len):
                        queue_front = queue.pop(0)
                        for j in range(len(adj[queue_front])):
                            if vis[adj[i][j]]==0:
                                vis[i] = 0
                                if hash_map.get(vis[adj[i][j]])!=None:
                                    cycle_found = True
                                    break
                                else:
                                    hash_map[adj[i][j]] = True
                                    queue.append(adj[i][j])
                        if cycle_found:
                            break
            if cycle_found:
                break
        
        return cycle_found
    

print(Solution().isCycle(5, [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]] ))
