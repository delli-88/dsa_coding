from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return None
        if head.next.next==None:
            head.next = head.next.next
            return head
        
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next

        return head
    
'''
Problem : https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list
TC - O(n)
SC - O(1)
Approach : 
We can use the fast and slow pointers here to find the mid,
and we keep track of slow's previous node
once we find slow, we delete that

'''