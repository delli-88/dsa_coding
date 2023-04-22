from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head== None or head.next==None:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False


'''
Problem : https://leetcode.com/problems/linked-list-cycle/
TC - O(n)
SC - O(1)
Approach:
We can use fast and slow pointers
If there is a cycle in a sll, then at some point of time, slow and fast pts must meet, so we return true
else fast reaches None, we return false
'''