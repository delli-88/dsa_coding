from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head==None or head.next==None:
            return None

        first_ptr = head
        last_ptr = head

        while n>0:
            last_ptr = last_ptr.next
            n-=1
        
        while last_ptr!=None and last_ptr.next!=None:
            first_ptr = first_ptr.next
            last_ptr = last_ptr.next
        
        first_ptr.next = first_ptr.next.next

        return head
        

'''
Problem : https://leetcode.com/problems/remove-nth-node-from-end-of-list
TC - O(n)
SC - O(1)
Approach:
We take two pointers
last_ptr will traverse through the list n positions
and we again travel the list, this time we start first_ptr from head and last_ptr from that pos where it travelled n places
and we inc both ptrs to next
by the time last_ptr reaches none, the first_ptr will reach n positions from last, and we delete 
'''