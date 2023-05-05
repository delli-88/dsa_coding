from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root==None:
            return []
        sol = []
        queue = [root]
        level_num = 0
        while queue:
            level = [] 
            i = len(queue)
            for _ in range(i):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                level.append(queue.pop(0).val)
            
            if level_num%2==0:
                sol.append(level)
            else:
                sol.append(level[::-1])
            level_num+=1
        return sol


'''
Problem : https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
Same as level order traversal
at odd places we reverse the list else we dont
'''