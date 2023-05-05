from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        pattern_hash = {}
        pattern_len = len(p)
        for i in range(pattern_len):
            pattern_hash[p[i]] = pattern_hash.get(p[i],0) +1
        
        str_window_hash = {}
        for i in range(pattern_len):
            str_window_hash[s[i]] = str_window_hash.get(s[i],0) +1
        
        anagrams_arr = []
        if pattern_hash==str_window_hash:
            anagrams_arr.append(0)
        
        for i in range(pattern_len,len(s)):
            str_window_hash[s[i]] = str_window_hash.get(s[i],0) +1
            str_window_hash[s[i-pattern_len]]-=1
            if str_window_hash[s[i-pattern_len]]==0:
                str_window_hash.pop(s[i-pattern_len])

            if pattern_hash==str_window_hash:
                anagrams_arr.append(i-pattern_len+1)
        
        return anagrams_arr
            


        

print(Solution().findAnagrams(s = "abab", p = "ab"))

'''
Problem : https://leetcode.com/problems/find-all-anagrams-in-a-string/
TC - O(s + p)
SC - O(p)
Approach :
we use hashing and sliding window here
we first hash the freq of pattern
then we travel through the string by window len of pattern and store all the freq of window len in another hash
check if two dicts are equal if yes, we append the index - len else we slide further
'''