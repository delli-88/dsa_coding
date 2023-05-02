class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for i in range(len(s)):
            if s[i]!='#':
                stack1.append(s[i])
            elif s[i]=="#" and stack1:
                stack1.pop()

        stack2 = []
        for i in range(len(t)):
            if t[i]!='#':
                stack2.append(s[i])
            elif t[i]=="#" and stack2:
                stack2.pop()

        if len(stack1)!=len(stack2) or stack1!=stack2:
            return False

        return True
        

'''
Problem : https://leetcode.com/problems/backspace-string-compare
TC - O(s + t)
SC - O(s + t)
Approach:
we iterate through the string s
    if the curr_char is not '#, we push it into the stack
    else if curr_char is '#' and stack is not empty, we pop the top
same goes for string t
we check if stack1 and stack2 are equal and return true

Another Approach:
we iterate through the string in reverse, then we will know how many backspace characters we have seen, 
and therefore whether the result includes our character. it takes O(1) space and O(s+t) time
'''
print(Solution().backspaceCompare(s = "a#c", t = "b"))