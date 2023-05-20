class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

from collections import deque

class Solution:
    def topViewBinaryTree(self, root):
        if not root:
            return []
        
        hash_map = {}
        queue = deque([(root, 0)])

        while queue:
            node, dist = queue.popleft()
            
            if dist not in hash_map:
                hash_map[dist] = node.val
            
            if node.left:
                queue.append((node.left, dist - 1))
            
            if node.right:
                queue.append((node.right, dist + 1))
        
        return [val for dist, val in sorted(hash_map.items())]

    def bottomView(self, root):
        if not root:
            return []
        
        hash_map = {}
        queue = deque([(root, 0)])

        while queue:
            node, dist = queue.popleft()
            hash_map[dist] = node.val
            
            if node.left:
                queue.append((node.left, dist - 1))
            
            if node.right:
                queue.append((node.right, dist + 1))
        
        return [val for dist, val in sorted(hash_map.items())]


'''
Approach:
For topViewBinaryTree function:

1.Initialize an empty dictionary hash_map to store the nodes at each horizontal distance from the root.
2.Create a deque queue and enqueue the root node along with its horizontal distance, which is initially 0.
3.While the queue is not empty, perform the following steps:
    3a.Dequeue a node node and its corresponding distance dist from the left of the queue.
    3b.If the current distance dist is not present in the hash_map, add the node's value to the hash_map with the distance dist as the key.
    3c.If the node has a left child, enqueue the left child along with dist - 1.
    3d.If the node has a right child, enqueue the right child along with dist + 1.
4.Sort the items of hash_map based on their keys in ascending order.
5.Extract the values from the sorted hash_map and return them as the top view of the binary tree.

For bottomView function:

1.Initialize an empty dictionary hash_map to store the nodes at each horizontal distance from the root.
2.Create a deque queue and enqueue the root node along with its horizontal distance, which is initially 0.
3.While the queue is not empty, perform the following steps:
    3a.Dequeue a node node and its corresponding distance dist from the left of the queue.
    3b.Update the hash_map with the node's value at the distance dist.
    3c.If the node has a left child, enqueue the left child along with dist - 1.
    3d.If the node has a right child, enqueue the right child along with dist + 1.
4.Sort the items of hash_map based on their keys in ascending order.
5.Extract the values from the sorted hash_map and return them as the bottom view of the binary tree.
'''