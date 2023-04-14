class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        
        start = 0
        freq = [-1]*127
        curr_len = 0
        max_len = 0

        for i in range(len(s)):
            if freq[ord(s[i])]>=start:
                start = freq[ord(s[i])] + 1
            freq[ord(s[i])] = i
            curr_len = i - start + 1
            max_len = max(max_len,curr_len)

        return max_len

"""
Problem : https://leetcode.com/problems/longest-substring-without-repeating-characters/
TC - O(n)
SC - O(1)
Optimal Approach :
We maintain a char array of size 127
we initialize the start to be 0, which is the start of our window
We loop through the string 
    at each iteration we update the index of that char in char array with its current index
    before updating, we check, if we have seen this in our window by checking with start, (if its index in char array is greater than start, that means we have already included it in our window)
        if we have seen it, we update our window size, we just move our start to the next index of already seen curr_char's index
    at each step we calc the curr_window_len and update max_len if necessary.
return max_len
"""

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        
        max_len = 0
        cur_len = 0
        left = 0
        char_dict = {}

        for i in range(len(s)):
            if char_dict.get(s[i]):
                while s[left]!=s[i]:
                    char_dict.pop(s[left])
                    cur_len-=1
                    left+=1
                left+=1
            else:
                char_dict[s[i]] = True
                cur_len+=1
            max_len = max(max_len,cur_len)
        return max_len
"""

print(Solution().lengthOfLongestSubstring(s = "dvdf"))