import os
import sys
from collections import *
from math import *
from typing import *
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

def maximumXor(A: List[int]) -> int:
    trie1 = Trie()

    for i in range(len(A)):
        trie1.insert(A[i])

    maxi = 0
    for i in range(len(A)):
        maxi = max(trie1.getMax(A[i]), maxi)
    
    return maxi

print(maximumXor[1,2,3,4])