class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxi = 0
        stack = [-1]

        valids = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for i in range(len(s)):
            if s[i] in valids.values():
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                curr = i - stack[-1]
                maxi = max(maxi,curr)
        return maxi

print(Solution().longestValidParentheses(s = ")()())"))

'''
Problem : https://leetcode.com/problems/longest-valid-parentheses
Approach : 
Same as vilid paranthesis
when we see a closed bracket, we can find the longest valid substring by substracting the curr_index with stack_top(which is invalid paranthesis)
'''