
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Solution:
    def printBoundaryView(self, root):
        if not root:
            return []
        
        boundary = []
        if root.left or root.right:
            boundary.append(root.data)
        
        self.get_left_boundaries(root.left, boundary)
        self.get_leaf_nodes(root, boundary)
        self.get_right_boundaries(root.right, boundary)

        return boundary

    def get_left_boundaries(self, root, boundary):
        if not root:
            return
        
        if root.left or root.right:
            boundary.append(root.data)
        
        if root.left:
            self.get_left_boundaries(root.left, boundary)
        else:
            self.get_left_boundaries(root.right, boundary)

    def get_right_boundaries(self, root, boundary):
        if not root:
            return

        if root.right:
            self.get_right_boundaries(root.right, boundary)
        else:
            self.get_right_boundaries(root.left, boundary)
        
        if root.left or root.right:
            boundary.append(root.data)

    def get_leaf_nodes(self, root, boundary):
        if not root:
            return
        
        if not root.left and not root.right:
            boundary.append(root.data)
        
        self.get_leaf_nodes(root.left, boundary)
        self.get_leaf_nodes(root.right, boundary)

'''
Problem :https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/0
TC - O(n)
SC - O(n)
Approach:
1.If the root is None, return an empty list.
2.Create an empty boundary list to store the boundary elements.
3.If the root has a left or right child, append the root's data to the boundary list.
4.Recursively traverse the left subtree:
    4a.If the current node has a left child, recursively call the function on the left child.
    4b.Otherwise, recursively call the function on the right child.
    4c.Append the current node's data to the boundary list.
5.Recursively traverse the right subtree:
    5a.If the current node has a right child, recursively call the function on the right child.
    5b.Otherwise, recursively call the function on the left child.
    5c.If the current node has a left or right child, append the current node's data to the boundary list.
6.Recursively traverse the tree to find the leaf nodes:
    6a.If the current node is a leaf node (has no left or right child), append its data to the boundary list.
7.Return the boundary list.

'''


'''

# iterative
class Solution:
    def printBoundaryView(self, root):
        if root is None:
            return []

        leftBoundaries = self.getLeftBoundaries(root.left)
        leafNodes = self.getLeafNodes(root)
        rightBoundaries = self.getRightBoundaries(root.right)

        return [root.data] + leftBoundaries + leafNodes + rightBoundaries

    def getLeftBoundaries(self, node):
        leftBoundaries = []
        while node and (node.left or node.right):
            leftBoundaries.append(node.data)
            node = node.left or node.right
        return leftBoundaries

    def getRightBoundaries(self, node):
        rightBoundaries = []
        while node and (node.left or node.right):
            rightBoundaries.append(node.data)
            node = node.right or node.left
        return rightBoundaries[::-1]

    def getLeafNodes(self, node):
        leafNodes = []
        stack = [node]
        while stack:
            current = stack.pop()
            if not current.left and not current.right:
                leafNodes.append(current.data)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return leafNodes

        
TC - O(n)
SC - O(n)
'''