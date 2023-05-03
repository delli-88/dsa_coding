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
'''


'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_ptr = len(s)-1
        s_hash = 0
        t_ptr = len(t)-1
        t_hash = 0
        while s_ptr>=0 or t_ptr>=0:
            while s_ptr>=0:
                if s[s_ptr]=='#':
                    s_hash+=1
                    s_ptr-=1
                elif s[s_ptr]!='#' and s_hash>0:
                    s_hash-=1
                    s_ptr-=1
                else:
                    break

            while t_ptr>=0:
                if t[t_ptr]=='#':
                    t_hash+=1
                    t_ptr-=1
                elif t[t_ptr]!='#' and t_hash>0:
                    t_hash-=1
                    t_ptr-=1
                else:
                    break

            if s_ptr>=0 and t_ptr>=0 and s[s_ptr]!=t[t_ptr]:
                return False

            if (s_ptr<0 and t_ptr>=0) or (t_ptr<0 and s_ptr>=0):
                return False
            
            s_ptr-=1
            t_ptr-=1

        return True

'''
'''
TC - O(s+t)
SC - O(1)
Approach:
we iterate through the string in reverse, then we will know how many backspace characters we have seen, 
and therefore whether the result includes our character.
We loop through the strings at at time
    for s,
        we look for first char which is to be considered,
    for t,
        we look for first char which is to be considered,
    
    then we check the chars if not equal we return false else continue

return true if entire strs are travelled 
'''            





print(Solution().backspaceCompare(s = "ab##", t = "c#d#"))