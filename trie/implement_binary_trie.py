class Node:
    def __init__(self) -> None:
        self.links = [None, None]
    def __repr__(self) -> str:
        return str(self.__dict__)
    
class Trie:

    def __init__(self) -> None:
        self.root = Node()

    def insert(self,num):
        curr_bit = self.root
        bit_mask = 1
        for i in range(31,-1,-1):
            is_curr_bit_set = 0
            if num & (bit_mask<<i)>0:
                is_curr_bit_set = 1

            if curr_bit.links[is_curr_bit_set]==None: #set
                curr_bit.links[is_curr_bit_set] = Node()

            curr_bit = curr_bit.links[is_curr_bit_set]

                
    def getMax(self,num):
        curr_root = self.root
        maxi = 0
        bit_mask = 1
        for i in range(31, -1, -1):
            is_num_curr_bit_set = 0
            if num & (bit_mask<<i)>0:
                is_num_curr_bit_set = 1

            curr_bit_opp = 1 -is_num_curr_bit_set 

            if curr_root.links[curr_bit_opp]!=None:
                maxi = maxi | (bit_mask<<i)
                curr_root = curr_root.links[curr_bit_opp]
            else:
                curr_root = curr_root.links[is_num_curr_bit_set]
        
        return maxi
    
    def __repr__(self) -> str:
        return str(self.__dict__)
    


'''
Approach : 
1.The Trie consists of nodes, where each node has two links: one for 0 and one for 1, representing the two possible bits in an integer (0 and 1).
2.The insert method is used to insert an integer into the Trie. It starts from the root and iterates over the 32 bits of the integer. For each bit, it checks if the corresponding link exists in the current node. If not, it creates a new node and sets the link. Then, it moves to the next node based on the current bit value.
3.The getMax method is used to find the maximum XOR value with a given integer. It starts from the root and iterates over the 32 bits of the integer in the opposite order. For each bit, it checks if the opposite bit link exists in the current node. If so, it updates the maximum value by setting the corresponding bit. Otherwise, it continues with the current bit link. Finally, it returns the maximum value.
'''