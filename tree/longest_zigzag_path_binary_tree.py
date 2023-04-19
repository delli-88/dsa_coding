from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return self.longestZigZagHelper(root, 0, None)

    def longestZigZagHelper(self, node,  go_left, steps):
        self.path_len = 0

        if node==None:
            return 0
        self.path_len = max(self.path_len, steps+1)
        if go_left:
            self.longestZigZagHelper(node.left, False,steps+1)
            self.longestZigZagHelper(node.right, True,1)
        else:
            self.longestZigZagHelper(node.left, False,1)
            self.longestZigZagHelper(node.right, True,steps+1)


        self.longestZigZagHelper(node.left, True,0)
        self.longestZigZagHelper(node.right, True,0)

        

        
print(Solution().longestZigZag())