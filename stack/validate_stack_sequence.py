from typing import List
class Solution:
    def validateStackSequences(self, pushed, popped):
        push_ptr, pop_ptr  = 0, 0
        for i in range(len(pushed)):
            pushed[push_ptr] = pushed[i]
            while push_ptr >= 0 and pushed[push_ptr] == popped[pop_ptr]:
                push_ptr-=1
                pop_ptr+=1
            push_ptr += 1
        if push_ptr==0:
            return True
        else:
            return False

"""
Problem : https://leetcode.com/problems/validate-stack-sequences/
TC - O(n)
SC - O(1)
Optimal Approach:
We use same approach as below, instead of using extra stack, we use the provided pushed stack as our stack
"""

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop_ptr = 0
        stack = []

        for push_ptr in range(len(pushed)):
            stack.append(pushed[push_ptr])
                        
            while stack and stack[-1]==popped[pop_ptr]:
                stack.pop()
                pop_ptr+=1
            
        if stack:
            return False
        else:
            return True
        
"""
TC - O(n)
SC - O(n)
Approach:
we take an empty stack
we loop through the pushed array
    we push each element into stack
    pop all elements if stack top is equal to popped_ptr
if stack is empty - retuen true
else return false
"""