from typing import List
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
Problem : https://leetcode.com/problems/validate-stack-sequences/
TC - O(n)
SC - O(n)
Optimal Approach:
we take an empty stack
we loop through the pushed array
    we push each element into stack
    pop all elements if stack top is equal to popped_ptr
if stack is empty - retuen true
else return false
"""