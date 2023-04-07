# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root,targetSum,0)

    def helper(self,node,target_sum,curr_sum):
        if node==None:
            return False

        if node.left==None and node.right==None:
            curr_sum+=node.val
            if curr_sum==target_sum:
                return True
            else:
                return False

        curr_sum+=node.val
        left = self.helper(node.left,target_sum,curr_sum)
        if left==True:
            return True
        right = self.helper(node.right,target_sum,curr_sum)
        if right==True:
            return True

        return False


"""
Problem : https://leetcode.com/problems/path-sum/description/
Approach :  Using Recursion
Base : If it is a Leaf Node
        Add curr node val
            if it is target : return True
            else : return False
Rec : 
    For every node add curr value
    and check its left node and right node recursively for target sum
"""
