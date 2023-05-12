from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sol_head = ListNode(-1)
        sol_tail = sol_head

        l1_ptr = l1
        l2_ptr = l2

        carry = 0

        while l1_ptr and l2_ptr:
            curr_sum = l1_ptr.val + l2_ptr.val + carry

            carry = curr_sum//10
            curr_digit = ListNode(curr_sum%10)

            sol_tail.next = curr_digit

            sol_tail = sol_tail.next
            l1_ptr = l1_ptr.next
            l2_ptr = l2_ptr.next
        

        while l1_ptr or l2_ptr or carry:
            curr_sum = (l1_ptr.val if l1_ptr else 0) + (l2_ptr.val if l2_ptr else 0) + carry
            carry = curr_sum // 10
            curr_digit = ListNode(curr_sum % 10)

            sol_tail.next = curr_digit
            sol_tail = sol_tail.next

            if l1_ptr:
                l1_ptr = l1_ptr.next
            if l2_ptr:
                l2_ptr = l2_ptr.next
        
        return sol_head.next


'''
Problem :
TC - O(max(l1,l2))
SC - O(max(l1,l2))
'''