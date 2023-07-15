from typing import List

class SegmentTree:
    def __init__(self, nums) -> None:
        self.nums = nums
        self.tree = [0 for _ in range(4*len(nums))]

    def build(self, node, start, end):
        if start==end:
            self.tree[node] = self.nums[start]
            return self.nums[start]
        
        mid = (start+end)//2
        left = self.build(2*node, start, mid)
        right = self.build(2*node+1, mid+1, end)
        self.tree[node] =  left+right 
        return self.tree[node]
    
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
            result = val - self.tree[node]
            self.tree[node] = val
            return result
        
        mid = (leftRange+rightRange)//2
        if ind<=mid:
            result = self.update(ind, val, leftRange, mid, 2*node)
        else:
            result = self.update(ind, val, mid+1, rightRange, 2*node+1)
        
        self.tree[node]+=result

        return result


    def __repr__(self) -> str:
        return str(self.__dict__)

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.segTree = SegmentTree(nums)
        self.segTree.build(1,0,len(nums)-1)
        

    def update(self, index: int, val: int) -> None:
        self.segTree.update(index,val,0,len(self.nums)-1,1)
        return 
        

    def sumRange(self, left: int, right: int) -> int:
        return self.segTree.sumQuery(left, right, 0, len(self.nums)-1, 1)
    
    def __repr__(self) -> str:
        return str(self.__dict__)
        


obj = NumArray([1,3,5,6,7,2])
print(obj.sumRange(0,5))
obj.update(2,6)
print(obj.sumRange(0,5))

'''
Problem : https://leetcode.com/problems/range-sum-query-mutable
Approach : 
1.The SegmentTree class is initialized with an array of numbers. It also contains a tree list that represents the segment tree.
2.The build method recursively builds the segment tree by dividing the range into two halves until reaching individual elements. The tree nodes store the sum of the corresponding range of numbers.
3.The sumQuery method performs a range sum query on the segment tree. It compares the query range with the current node's range to determine if the current node's value is fully contained within the query range, partially intersects with the query range, or is completely outside the query range. Based on this comparison, the method traverses the left and right subtrees recursively and returns the sum of their results.
4.The update method updates the value of a specific index in the segment tree and maintains the sum property of the tree. It recursively traverses the tree to find the corresponding leaf node and updates it. As it backtracks, it adjusts the values of the parent nodes by adding the difference between the new value and the old value.
5.The NumArray class represents the interface for the range sum query and update operations. It initializes a segment tree using the provided array of numbers and builds the tree.
6.The update method in the NumArray class updates a specific index in the original array and reflects the changes in the segment tree by calling the update method of the segment tree.
7.The sumRange method in the NumArray class performs a range sum query on the original array by calling the sumQuery method of the segment tree.

In summary, the code constructs a segment tree from the given array and provides methods to update the array and perform range sum queries efficiently using the segment tree. The NumArray class acts as a wrapper for the segment tree operations.

'''
