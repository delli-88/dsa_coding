class Solution:
    def longestKSubstr(self, s, k):
        dist_chars = 0
        chars_map = {}
        curr_window_len = 0
        max_len = -1

        for i in range(len(s)):
            if chars_map.get(s[i]):
                chars_map[s[i]]+=1
                curr_window_len+=1
            else:
                while dist_chars>=k:
                    chars_map[s[left]]-=1
                    curr_window_len-=1
                    if chars_map[s[left]]==0:
                        dist_chars-=1
                        chars_map.pop(s[left])
                    left+=1 
                chars_map[s[i]] = 1
                curr_window_len+=1
                dist_chars += 1
            if dist_chars==k:
                max_len = max(max_len,curr_window_len)
                
        return max_len
    
"""
Problem : https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1
TC - O(n)
SC - O(26) -> O(1)
Approach:
We a map to hold the number of distinct characters in the window, as well as a variable to hold the length of the longest substring with at most K distinct chars seen so far.
We start traversing, We add elements to the map with the traversal, checking to ensure that the number of distinct characters does not exceed K. Parallely, we also keep updating len with each element added to the map.
As soon as the map exceeds K distinct characters, we remove the first character from the window, which is left.
This process is followed until we reach the end of the string.
"""