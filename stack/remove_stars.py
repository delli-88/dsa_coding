class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i]!="*":
                stack.append(s[i])
            else:
                stack.pop()
        return "".join(stack)
    
"""
Problem: https://leetcode.com/problems/removing-stars-from-a-string/
TC - O(n)
SC - O(n)
Approach:
We can use a stack.
travel the string
    if the curr char is a "*" then pop the stack top
    else push the curr char into the stack
return the tack in form of string
"""