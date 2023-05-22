
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return str(self.__dict__)

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root==None:
            return None
        
        arr = []
        self.getInorderTraversalArr(root,arr)

        newBst = self.createBST(arr,0,len(arr)-1)
        
        return newBst
    
    def createBST(self,arr,start,end):
        if start>end:
            return None
        
        if start==end:
            return TreeNode(arr[start])

        mid = (start+end)//2
        
        left = self.createBST(arr,start,mid-1)
        right = self.createBST(arr,mid+1,end)

        new_head = TreeNode(arr[mid])
        new_head.left = left
        new_head.right = right

        return new_head

    def getInorderTraversalArr(self,root,arr):

        if root==None:
            return arr

        self.getInorderTraversalArr(root.left,arr)
        arr.append(root.val)
        self.getInorderTraversalArr(root.right,arr)

        return arr


sol = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

# print(sol.getInorderTraversalArr(root),[])
print(sol.balanceBST(root))
# print(sol.getInorderTraversalArr(sol.balanceBST(root)),[])

'''
Problem : https://leetcode.com/problems/balance-a-binary-search-tree/
TC - O(n)
SC - O(n)
Approach:
1.Initialize an empty array arr to store the in-order traversal of the original tree.
2.Perform an in-order traversal of the original tree and append the node values to the arr array.
3.Define a recursive function createBST that takes the arr, start index, and end index as parameters.
4.In the createBST function, if the start index is greater than the end index, return None.
5.If the start index is equal to the end index, create a new tree node with the value at the start index of arr and return it.
6.Calculate the mid index as the average of the start and end indices.
7.Recursively call the createBST function with the left half of the arr (from start to mid-1) to construct the left subtree.
8.Recursively call the createBST function with the right half of the arr (from mid+1 to end) to construct the right subtree.
9.Create a new tree node with the value at the mid index of arr and assign the left and right subtrees.
10.Return the newly created node.
11.Call the createBST function with the arr, start index 0, and end index len(arr)-1 to construct the balanced binary search tree.
12.Return the newly constructed balanced binary search tree.
'''