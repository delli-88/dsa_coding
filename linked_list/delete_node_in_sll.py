# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextNode = node.next
        node.val = nextNode.val
        node.next = nextNode.next
        nextNode.next = None
        del(nextNode)
        return
    
"""
Problem : https://leetcode.com/problems/delete-node-in-a-linked-list/
Approach:
As head is not given
We have node to be deleted
we copy the nextNode val of node to be deleted and copy it to the node to be deleted
link the node to be deleted next to next of next node.
delete the nextnode and point to none.
"""