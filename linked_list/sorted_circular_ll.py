class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def insertIntoSortedCircularList(head: ListNode, insertVal: int) -> ListNode:
  new_node = ListNode(insertVal)
  if head==None:
    new_node.next = new_node
    return new_node
  curr = head
  while curr.next!=head:
    if curr.val <= insertVal <= curr.next.val:
        break
    if curr.next.val < curr.val and (insertVal < curr.next.val or insertVal > curr.val):
        break
    curr = curr.next
  new_node.next = curr.next
  curr.next = new_node
  return head


'''
Problem : https://www.geeksforgeeks.org/sorted-insert-for-circular-linked-list/
TC - O(n)
SC - O(1)
Approach :
We traverse through the ll 
At every elem,
we check if the insertVal is in between curr elem and next to curr elem, if yes we break 
or if it is a tail, and the  insertVal is either greatest or smallest, in both cases we break
else we move to next

after the while loop, we got the position to be inserted, we can just insert and return head


'''

