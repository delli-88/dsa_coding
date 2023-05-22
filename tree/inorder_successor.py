class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
                
def inorderSuccessor(root: TreeNode, node: TreeNode) -> TreeNode:
    
    successor = findSuccessor(root,node,None)

    if successor==None:
        return TreeNode(-1)
    
    return successor

def findSuccessor(node,x,successor):

    if not node:
        return successor

    if node.val > x.val:
        return findSuccessor(node.left,x,node)
    else:
        return findSuccessor(node.right,x,successor)
    

'''
Approach:
Problem : https://practice.geeksforgeeks.org/problems/inorder-successor-in-bst/1
If the given node has a right child, then the inorder successor is the leftmost node in the right subtree.
If the given node does not have a right child, then the inorder successor is the closest ancestor for which the given node is in its left subtree.
TC - O(n)
Sc - O(1)
'''