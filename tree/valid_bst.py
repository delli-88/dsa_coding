from typing import List,Optional
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, -inf, inf)
    
    def isValidBSTHelper(self, root, min_val, max_val):

        if root==None:
            return True
        
        if root.val<min_val or root.val>max_val:
            return False

        left = self.isValidBSTHelper(root.left,min_val,root.val)

        right = self.isValidBSTHelper(root.right,root.val,max_val)

        if left and right:
            return True

        return False


'''
Problem : https://leetcode.com/problems/validate-binary-search-tree

Recurrence Relation - 2T (N/2) + 1
TC - O(n)
SC - O(n) (avg-O(logn) call stack space)
Approach :
1.Implement the isValidBSTHelper method with the following parameters: root, min_val, and max_val.
2.Base case: If the root is None, return True since an empty tree is considered a valid BST.
3.Check if the root value is less than or equal to the min_val or greater than or equal to the max_val. If so, return False as the current node violates the BST property.
4.Recursively call the isValidBSTHelper method for the left subtree with the min_val unchanged and the max_val updated to the current root value.
5.Recursively call the isValidBSTHelper method for the right subtree with the min_val updated to the current root value and the max_val unchanged.
6.Check if both the left and right subtree validations return True. If so, return True indicating that the current subtree is a valid BST.
7.If any of the validations fail, return False as the tree is not a valid BST.
'''


'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        self.isValidBSTHelper(root,arr)
        return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))
    
    def isValidBSTHelper(self,root,arr):
        if root==None:
            return arr

        self.isValidBSTHelper(root.left,arr)
        arr.append(root.val)
        self.isValidBSTHelper(root.right,arr)

        return arr

TC - O(n)
sc - O(n)
Approach :
For a tree to be a valid BST, its InOrder traversal should be a sorted list.
'''
print(Solution().isValidBST())

