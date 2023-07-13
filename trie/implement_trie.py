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
                return False
            curr_node = curr_node.links[curr_letter_idx]
        if curr_node.flag:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for i in range(len(prefix)):
            curr_letter = prefix[i]
            curr_letter_idx = ord(curr_letter)-ord("a") 
            if curr_node.links[curr_letter_idx]==None:
                return False
            curr_node = curr_node.links[curr_letter_idx]
        return True
    
    def __repr__(self) -> str:
        return str(self.__dict__)
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
obj.insert("apps")
obj.insert("apap")
obj.insert("abc")
print(obj.search("apps"))
print(obj.startsWith("appsa"))

# print(obj)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

'''
Aproach :
1.Create a Node class with two attributes: links and flag. The links attribute is a list of size 26, initialized with None, to represent the links to child nodes. The flag attribute indicates whether a word ends at the current node.
2.Create a Trie class with the following methods:
    a.__init__(): Initialize the Trie by creating an empty root node.
    b.insert(word): Insert a word into the Trie. Traverse the Trie from the root, creating new nodes for each character if necessary, and marking the last node as the end of a word.
    c.search(word): Check if a word exists in the Trie. Traverse the Trie from the root, following the links for each character, and return True if the word ends at a node with the flag set to True.
    d.startsWith(prefix): Check if there is any word in the Trie that starts with the given prefix. Traverse the Trie from the root, following the links for each character, and return True if the prefix is valid (all characters exist in the Trie).
3.In the insert method, iterate over each character in the word. Calculate the index of the character by subtracting the ASCII value of 'a' from the current character's ASCII value. Check if the link for that character is None, indicating that it doesn't exist, and create a new Node if necessary. Move to the next node and repeat the process until all characters in the word are processed. Finally, mark the last node as the end of a word by setting its flag to True.
4.In the search method, iterate over each character in the word and follow the corresponding links in the Trie. If, at any point, a link is None, return False as the word doesn't exist in the Trie. If the traversal reaches the end of the word and the node's flag is True, return True to indicate that the word is found.
5.In the startsWith method, iterate over each character in the prefix and follow the corresponding links in the Trie. If, at any point, a link is None, return False as the prefix is not a valid prefix in the Trie. If the traversal completes without encountering None, return True to indicate that there are words in the Trie that start with the given prefix.
'''