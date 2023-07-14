from typing import List
class Node:
    def __init__(self) -> None:
        self.links = [None for _ in range(26)]
        self.flag = False
    
    def __repr__(self) -> str:
        return str(self.__dict__)

class Trie:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        curr_node = self.root
        for i in range(len(word)):
            curr_letter = word[i]
            curr_letter_idx = ord(curr_letter)-ord("a")

            if curr_node.links[curr_letter_idx]==None:
                curr_node.links[curr_letter_idx] = Node()        

            curr_node = curr_node.links[curr_letter_idx]
        curr_node.flag = True
        return
        

    def search(self, word: str) -> bool:
        curr_node = self.root
        for i in range(len(word)):
            curr_letter = word[i]
            curr_letter_idx = ord(curr_letter)-ord("a") 
            if curr_node.links[curr_letter_idx]==None:
                return word
            curr_node = curr_node.links[curr_letter_idx]
            if curr_node.flag:
                return word[:i+1]
        return word


    
    def __repr__(self) -> str:
        return str(self.__dict__)
        

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        myTrie = Trie()
        for i in range(len(dictionary)):
            myTrie.insert(dictionary[i])
        
        words = sentence.split(" ")

        sol_words = []

        for i in range(len(words)):
            sol_words.append(myTrie.search(words[i]))
        
        return " ".join(sol_words)

        
print(Solution().replaceWords(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"))