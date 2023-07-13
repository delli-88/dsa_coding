from os import *
from sys import *
from collections import *
from math import *

class Node:
    def __init__(self) -> None:
        self.links = [None for _ in range(26)]
        self.endsWith = 0
        self.countPrefix = 0
    
    def __repr__(self) -> str:
        return str(self.__dict__)

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr_node = self.root
        
        for i in range(len(word)):
            curr_word = word[i]
            curr_idx = ord(curr_word)- ord("a")

            if curr_node.links[curr_idx]==None:
                curr_node.links[curr_idx] = Node()

            curr_node = curr_node.links[curr_idx]
            curr_node.countPrefix+=1
        
        curr_node.endsWith+=1
            
    def countWordsEqualTo(self, word):
        curr_node = self.root
        
        for i in range(len(word)):
            curr_word = word[i]
            curr_idx = ord(curr_word)- ord("a")

            if curr_node.links[curr_idx]==None:
                return 0

            curr_node = curr_node.links[curr_idx]
        
        return curr_node.endsWith

    def countWordsStartingWith(self, word):
        curr_node = self.root
        
        for i in range(len(word)):
            curr_word = word[i]
            curr_idx = ord(curr_word)- ord("a")

            if curr_node.links[curr_idx]==None:
                return 0

            curr_node = curr_node.links[curr_idx]
        
        return curr_node.countPrefix

    def erase(self, word):
        curr_node = self.root
        
        for i in range(len(word)):
            curr_word = word[i]
            curr_idx = ord(curr_word)- ord("a")

            if curr_node.links[curr_idx]==None:
                return

            curr_node = curr_node.links[curr_idx]
            curr_node.countPrefix-=1
        
        curr_node.endsWith-=1

        return

    
    def __repr__(self) -> str:
        return str(self.__dict__)
    
'''
Approach :
1.Import necessary modules: Import the required modules such as os, sys, collections, and math based on the usage in the code.
2.Create a Node class: Define a Node class with three attributes: links, endsWith, and countPrefix. The links attribute is a list of size 26, initialized with None, to represent the links to child nodes. The endsWith attribute keeps track of the number of words that end at the current node. The countPrefix attribute stores the count of words that have the current node as a prefix.
3.Create a Trie class: Define a Trie class with the following methods:
    a.__init__(): Initialize the Trie by creating an empty root node of type Node.
    b.insert(word): Insert a word into the Trie. Traverse the Trie from the root, creating new nodes for each character if necessary, and update the countPrefix and endsWith attributes accordingly.   
    c.countWordsEqualTo(word): Count the number of words in the Trie that are equal to the given word. Traverse the Trie from the root, following the links for each character, and return the endsWith count of the last node reached.
    d.countWordsStartingWith(word): Count the number of words in the Trie that have the given word as a prefix. Traverse the Trie from the root, following the links for each character, and return the countPrefix count of the last node reached.
    e.erase(word): Remove a word from the Trie. Traverse the Trie from the root, following the links for each character, and update the countPrefix and endsWith attributes accordingly.
4.In the insert method, iterate over each character in the word. Calculate the index of the character by subtracting the ASCII value of 'a' from the current character's ASCII value. Check if the link for that character is None, indicating that it doesn't exist, and create a new Node if necessary. Move to the next node and update the countPrefix attribute to reflect the addition of a new word with the current prefix. Finally, update the endsWith attribute of the last node to indicate the end of a word.
5.In the countWordsEqualTo method, iterate over each character in the word and follow the corresponding links in the Trie. If, at any point, a link is None, return 0 as there are no words equal to the given word in the Trie. If the traversal reaches the end of the word, return the endsWith count of the last node reached.
6.In the countWordsStartingWith method, iterate over each character in the word and follow the corresponding links in the Trie. If, at any point, a link is None, return 0 as there are no words with the given word as a prefix in the Trie. If the traversal completes without encountering None, return the countPrefix count of the last node reached.
7.In the erase method, iterate over each character in the word and follow the corresponding links in the Trie. If, at any point, a link is None, return. Move to the next node and update the countPrefix attribute to reflect the removal of a word with the current prefix. Finally, update the endsWith attribute of the last node to indicate the removal of a word.
'''