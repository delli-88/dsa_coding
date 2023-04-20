
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        queue = [(root,0)]
        max_width = 0
        while queue:
            
            queue_len = len(queue)
            _, level_start_ind = queue[0]
            for _ in range(queue_len):
                queue_start, curr_ind = queue.pop(0)
                if queue_start.left:
                    queue.append((queue_start.left,curr_ind*2))
                if queue_start.right:
                     queue.append((queue_start.right,(curr_ind*2)+1))
            
            curr_level_width = curr_ind - level_start_ind + 1
            max_width = max(max_width, curr_level_width)
        
        return max_width
    
'''
Problem : https://leetcode.com/problems/maximum-width-of-binary-tree
Approach :
We can use a level order traversal
We acn use a queue to store the level nodes with corresponding indices
at each level we first copy the level start index
after entire level is traversed, we have last nodes index
so we can calc the width using, last nodes index- first nodes index
and find max at each level
'''
                    
                
