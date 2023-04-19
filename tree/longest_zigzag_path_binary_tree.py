from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.pathLength = 0
        
        def dfs(node, goLeft, steps):
            if node:
                self.pathLength = max(self.pathLength, steps)
                if goLeft:
                    dfs(node.left, False, steps + 1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, steps + 1)
        
        dfs(root, True, 0)
        return self.pathLength

'''
Problem :
Approach :
We use dfs
If goLeft is true, the zigzag path will continue to the left. We can't go left in the next step to continue this zigzag path because we're already going left in this step. As a result, we call dfs(node.left, false, steps + 1). We passed steps + 1 because we kept going in a zigzag pattern.
opposite goes if goLeft is false
'''
        

        
print(Solution().longestZigZag())