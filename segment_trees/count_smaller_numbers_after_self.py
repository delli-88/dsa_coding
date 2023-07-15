from typing import List
class SegmentTree:
    def __init__(self, nums, min1, max1) -> None:
        self.nums = nums
        self.tree = [0 for _ in range(4*(max1-min1))]

    
    def sumQuery(self, leftQuery, rightQuery, leftRange, rightRange, node):

        if leftRange>=leftQuery and rightRange<=rightQuery:
            return self.tree[node]
        
        if leftRange>rightQuery or rightRange<leftQuery:
            return 0
        
        mid = (leftRange + rightRange)//2
        leftSum = self.sumQuery(leftQuery, rightQuery, leftRange, mid, 2*node)
        rightSum = self.sumQuery(leftQuery, rightQuery, mid+1, rightRange, 2*node+1)

        return leftSum+rightSum
    
    def update(self, ind, val, leftRange, rightRange, node):
        if leftRange==ind and rightRange==ind:
            self.tree[node]+=1
            return 
        
        mid = (leftRange+rightRange)//2
        if ind<=mid:
            self.update(ind, val, leftRange, mid, 2*node)
        else:
            self.update(ind, val, mid+1, rightRange, 2*node+1)

        self.tree[node]+=1

        return 


    # def __repr__(self) -> str:
    #     return str(self.__dict__)
    
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        min1 = min(nums)
        max1 = max(nums)

        sol = [0 for _ in range(len(nums))]
        if min1==max1:
            return sol
        segTree = SegmentTree(nums, min1, max1)
        for i in range(len(nums)-1,-1,-1):
            sol[i] = segTree.sumQuery(min1,nums[i]-1,min1,max1,1)
            segTree.update(nums[i],1,min1, max1, 1)        
        return sol
    
    # def __repr__(self) -> str:
    #     return str(self.__dict__)


print(Solution().countSmaller([5,2,6,1]))

'''
Problem : https://leetcode.com/problems/count-of-smaller-numbers-after-self/
Approach : 
1.Define the SegmentTree class, which initializes the segment tree with an array of numbers and the minimum and maximum values in the array.
2.Implement the sumQuery method in the SegmentTree class, which calculates the sum of values in a given range [leftQuery, rightQuery] within the segment tree.
3.Implement the update method in the SegmentTree class, which updates the segment tree by incrementing the values at a given index ind.
4.Define the Solution class, which contains the countSmaller method. This method takes an input array of numbers and returns a new array sol where sol[i] represents the count of smaller elements to the right of nums[i].
5.Find the minimum and maximum values in the input array nums and initialize the SegmentTree with these values.
6.Iterate through the nums array in reverse order. For each element nums[i], use the sumQuery method to calculate the count of smaller elements by querying the segment tree with the range [min1, nums[i]-1].
7.Update the segment tree using the update method by incrementing the count at index nums[i].
8.Return the sol array, which contains the counts of smaller elements.
'''