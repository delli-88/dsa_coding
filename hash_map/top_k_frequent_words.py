from typing import List
from functools import cmp_to_key
class Solution:

    def compare (self,item1,item2):
        if item1[1]>item2[1]:
            return -1
        elif item1[1]<item2[1]:
            return 1
        
        if item1[0]<item2[0]:
            return -1
        else:
            return 1

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_freq_dict = {}

        for i in range(len(words)):
            words_freq_dict[words[i]] = words_freq_dict.get(words[i],0) +1
        
        words_sorted_arr = [item1 for item1,item2 in sorted(words_freq_dict.items(), key=cmp_to_key(self.compare))][:k]
        return words_sorted_arr

'''
Problem : https://leetcode.com/problems/top-k-frequent-words/
TC - O(nlogn)
SC - O(n)
Approach :
We can use hash-map to store frequencies of the words
We can use a library and a function which gives us a sorted list in descending order of freqencies in lexicographical order
'''

print(Solution().topKFrequent(["coding","love","i","leetcode","i","love"],2))