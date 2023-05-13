class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_list(self, node1, node2):
        list1 = node1
        list2 = node2
        merged = ListNode(-1)
        curr = merged

        while list1 and list2:

            if list1.val<list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        if list1:
            curr.next = list1
        
        if list2:
            curr.next = list2

        return merged.next

        
    def get_middle(self,node):

        slow = node
        fast = node
        slow_prev = None

        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next
        
        return  slow_prev
    
    def sortList(self,ll):
        if ll==None or ll.next==None:
            return ll
        
        mid = self.get_middle(ll)
        left = ll
        right = mid.next
        mid.next = None

        sorted_left = self.sortList(left)
        sorted_right = self.sortList(right)

        return self.merge_list(sorted_left,sorted_right)