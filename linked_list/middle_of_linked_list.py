# Definition for singly-linked list.
from typing import List,Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
"""
Approach:
Fast and slow pointer
slow pointer moves 1 step
fast pointer moves 2 steps
By the time fast pointer reaches end, slow pointer will be in middle
"""