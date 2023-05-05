
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        node_map = {}
        self.findModeHelper(root, node_map)
        maxi = max(node_map.values())
        sol = []
        for k,v in node_map.items():
            if v==maxi:
                sol.append(k)
        return sol
    
    def findModeHelper(self, node, node_map):
        if node==None:
            return node_map

        node_map[node.val] = node_map.get(node.val, 0) + 1

        self.findModeHelper(node.left, node_map)
        self.findModeHelper(node.right, node_map)

        return node_map

"""
Approach:
We recursively travel the tree and update hash_map with freq,
and travel hash_map to find all modes
"""
