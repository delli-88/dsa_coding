
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head

'''
Problem : https://leetcode.com/problems/odd-even-linked-list/
TC - O(n)
SC - O(1)
Approach :
We fist take odd and even elements as pointers
and while even is still present we loop
we know the odd's next val will be the even nodes next and vice versa and we use this property
we are storing all odd indices in add pointer and even in even ptr
and we are linking them
'''