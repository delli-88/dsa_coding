from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr_node = head
        hash_list = {}

        copy_head = Node(-1)
        copy_tail = copy_head

        while curr_node:
            copy_tail.next = Node(curr_node.val)
            hash_list[curr_node] = copy_tail.next

            curr_node = curr_node.next
            copy_tail = copy_tail.next

        curr_ori = head
        curr_copy = copy_head.next
        while curr_ori:
            curr_copy.random = hash_list.get(curr_ori.random)
            
            curr_ori = curr_ori.next
            curr_copy = curr_copy.next

        return copy_head.next



print(Solution().copyRandomList(head = [[7,None],[13,0],[11,4],[10,2],[1,0]]))

'''
Problem : https://leetcode.com/problems/copy-list-with-random-pointer
TC - O(n)
SC - O(n)
Approach :
For one traversal we create a new node, and add it as a value to the original node as key in a hash map to keep copy

for 2nd traversal, we add random pointer(we can get that by accessing the hashmap)

'''


