from math import inf
from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #sort the array
        people.sort()
        low = 0
        high = len(people)-1
        boats = 0
        # check the low and high people if they are less than limit
        # if yes, send both of them in a boat, increase low, decrease high,
        # if no, send the high weight person in a single boat and decrease high
        # continue till low>high
        while low<=high:
            if people[low]+people[high]<=limit:
                low+=1
            high-=1
            boats+=1
        
        return boats


        #Recursion TLE
        """Approach
        For every pos there will be pos to len options.
        so, check if each weight is less than limit or not
        if yes, remove that particular  weight and check the next elements recursively
        if not pass the entire array and check recursively
        It will result in TLE
        """
# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         boats = [0]
#         self.helper(people,limit,boats,0)
#         return boats[0]
    
#     def helper(self,people,limit,boats,pos):
#         if pos >= len(people)-1:
#             if pos== len(people)-1:
#                 return 1
#             return 0
#         min_f = inf
#         for i in range(pos+1,len(people)):
#             if people[pos]+people[i]<=limit:
#                 popped = people.pop(i)
#                 min1 = self.helper(people,limit,boats,pos+1)
#                 people.insert(i,popped)
#             else:
#                 min1 = self.helper(people,limit,boats,pos+1)
#             min_f = min(min_f,min1)
#         boats[0] = 1 + min_f
#         return boats[0]


# Problem : https://leetcode.com/problems/boats-to-save-people/
