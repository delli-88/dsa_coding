from typing import Optional
class ListNode:  
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Recursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head

        curr_node_next = head.next
        reversed_list = self.reverseList(head.next)
        head.next = None
        curr_node_next.next = head

        head = reversed_list
        return head


'''
Problem : https://leetcode.com/problems/reverse-linked-lis
TC - O(n)
SC - O(1)
Approach:
In this recursive approach,
We copy the head's next to curr_node_next pointer, this node becomes a tail after recursion
we do recursion on heads next and expects the recursion fun to bring us a list by reversing all the nodes from heads next to tail
So we just need to connect our curr head to the tails next which we have stored in curr_node_next, before that we make heads next to none
the list brought to us by recursions first node will be our new head, so return that.

'''

'''
# iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        
        prev = None
        curr = head
        
        while curr:

            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        head = prev

        return head

TC - O(n)
SC - O(1)
Approach : 
We take three pointers
curr is a pointer to keep track of current nodes. Set it to head.
prev is a pointer to keep track of previous nodes. Set it to None.
next_node is a pointer to keep track of the next nodes.

Set next_node to point next node to node pointed by curr.
Change link between nodes pointed by curr and prev.
Update prev to curr and curr pointer to next_node.
loop until curr reaches None.

Set head as prev_node. This makes the head point at the last node.
'''

