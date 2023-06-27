from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        
        if endWord not in word_set:
            return 0
        
        queue = deque()
        queue.append((beginWord, 1))
        
        while queue:
            queue_len = len(queue)

            for _ in range(queue_len):
                word, seq_len = queue.popleft()
                
                for j in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        curr_word = word[:j] + char + word[j+1:]
                        
                        if curr_word == endWord:
                            return seq_len + 1
                        
                        if curr_word in word_set:
                            queue.append((curr_word, seq_len + 1))
                            word_set.remove(curr_word)
        
        return 0

                            
print(Solution().ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))

'''
Problem : https://leetcode.com/problems/word-ladder/
TC - O(M^2 * N)
SC - O(N)
Approach :
1.Create a set word_set from the given wordList to allow for faster lookup of words.
2.Check if endWord is present in word_set. If not, it is impossible to transform beginWord into endWord, so return 0.
3.Create a queue and enqueue a tuple (beginWord, 1), where the second element represents the current sequence length.
4.While the queue is not empty, do the following:
    a.Get the current word and sequence length from the front of the queue.
    b.Iterate over each character position in the word.
    c.For each character position, replace the character with each lowercase alphabet letter.
    d.If the resulting word is equal to endWord, return the sequence length plus 1, as we have reached the end word.
    e.If the resulting word is present in word_set, enqueue it into the queue with the updated sequence length and remove it from word_set to avoid revisiting.
5.If the queue is exhausted and we have not found endWord, it means it is impossible to transform beginWord into endWord, so return 0.
'''