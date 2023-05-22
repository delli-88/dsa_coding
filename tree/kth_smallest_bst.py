from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.__dict__)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [None]
        count = [0]
        self.inorder(root,k,count,res)
        return res[0]

    def inorder(self,root,k,count,res):
        if root==None:
            return 
        self.inorder(root.left,k,count,res)
        count[0]+=1
        if count[0]==k:
            res[0] = root.val
            return 
        self.inorder(root.right,k,count,res)

'''
Problem : https://leetcode.com/problems/kth-smallest-element-in-a-bst/
TC - O(n)
SC - O(H) height for recursive call stack
Approach :
The main idea of the approach is to perform an inorder traversal of the binary search tree while keeping track of the count of visited nodes. When the count becomes equal to k, the current node value is the k-th smallest element.
1.Initialize an empty list res to store the result.
2.Initialize a counter count to keep track of the number of nodes visited.
3.Call the inorder function with the root of the binary search tree, the value of k, the count variable, and the res list.
4.In the inorder function:
    4a. Check if the current node is None. If so, return.
    4b. Recursively traverse the left subtree by calling inorder on root.left, passing the same arguments.
    4c. Increment the count by 1.
    4d. Check if the current count is equal to k. If so, set the value of the current node as the result res[0].
    4e. Recursively traverse the right subtree by calling inorder on root.right, passing the same arguments.
5.After the recursive calls in the inorder function, the value of the k-th smallest element will be stored in res[0].
6.Return the value stored in res[0].
'''

sol = Solution()

root = TreeNode(5)
root.right = TreeNode(6)
root.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(1)

print(sol.kthSmallest(root,3))