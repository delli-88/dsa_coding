from typing import List,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return str(self.__dict__)

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hash_map_inorder = {}
        for i in range(len(preorder)):
            hash_map_inorder[inorder[i]] = i 
        return self.buildTreeHelper(preorder,inorder,0,0,len(preorder)-1,hash_map_inorder)

    def buildTreeHelper(self, preorder, inorder, root_pos_pre, start, end, hash_map_inorder): 
        if start>end:
            return None 
        if start==end:
            root = TreeNode(inorder[start])
            return root
        
        root_pos_in = hash_map_inorder[preorder[root_pos_pre]]
        left = self.buildTreeHelper(preorder, inorder, root_pos_pre+1,start,root_pos_in-1,hash_map_inorder)
        right = self.buildTreeHelper(preorder, inorder, root_pos_pre+root_pos_in-start+1,root_pos_in+1,end,hash_map_inorder)

        
        root = TreeNode(preorder[root_pos_pre])
        root.left = left
        root.right = right

        return root

'''
Problem : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
Recurrence - 2T(N/2)+1
TC - O(n)
SC - O(n)
Approach :
1)The buildTree function takes the preorder and inorder traversal lists as input and initializes a hashmap to store the indices of elements in the inorder list.
2)It calls the buildTreeHelper function with the initial parameters - the preorder list, inorder list, root position in the preorder list, start and end indices for the inorder list, and the hashmap.
3)Inside the buildTreeHelper function:
    a)If the start index is greater than the end index, it means there are no elements left to construct the tree, so it returns None.
    b)If the start and end indices are the same, it means there is only one element left, so it creates a new tree node with that element and returns it.
    c)Otherwise, it finds the position of the root element in the inorder list using the hashmap.
    d)It recursively calls buildTreeHelper for the left subtree, passing the appropriate indices and updates the root position for the preorder list.
    e)It recursively calls buildTreeHelper for the right subtree, passing the appropriate indices and updates the root position for the preorder list.
    d)Finally, it creates a new tree node with the current root element, sets its left and right subtrees, and returns the root node.
4)The buildTree function returns the root of the constructed binary tree.
'''
print(Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]))


