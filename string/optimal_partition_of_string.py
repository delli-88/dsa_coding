from typing import List
class Solution:
    def partitionString(self, s: str) -> int:
        letter_dict = {}
        min_count = 1
        for letter in range(len(s)):
            if letter_dict.get(s[letter]):
                min_count+=1
                letter_dict.clear()
            letter_dict[s[letter]] = True
        return min_count
    
"""
Problem : https://leetcode.com/problems/optimal-partition-of-string/
Approach
    We initialize min count of required substring to 1
    and an empty dictionary to store the substrings
    We loop through the given string once
        check if the char is present in dict
        if yes, clear the dictionary and inc the sub string count and add the char into the current empty dict
        if no, just add into the dict
    return the count

TC - O(n)
SC - min(O(n),O(26)) -> O(1)
"""
print(Solution().partitionString(s = "hdklqkcssgxlvehva"))