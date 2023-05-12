from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sol_head = ListNode(-1)
        sol_tail = sol_head

        l1_ptr = self.create_deep_copy(l1)
        l2_ptr = self.create_deep_copy(l2)
        l1_ptr = self.reverse_list(l1_ptr)
        l2_ptr = self.reverse_list(l2_ptr)
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
        
        sol_head = self.reverse_list(sol_head.next)
        return sol_head
    
    def reverse_list(self, head):

        if head==None or head.next==None:
            return head

        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        
        return prev

    # creating the copy of linked list so that original structure of ll is not modified
    def create_deep_copy(self, head):
        if head == None:
            return None

        curr = head

        new_head = ListNode(curr.val)
        new_tail = new_head

        curr = curr.next

        while curr:
            new_node = ListNode(curr.val)
            new_tail.next = new_node
            new_tail = new_tail.next
            curr = curr.next
        
        return new_head
    
'''
Problem : https://leetcode.com/problems/add-two-numbers-ii
TC - O(max(l1,l2))
SC - O(max(l1,l2))
'''