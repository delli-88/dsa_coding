from typing import List

class SegmentTree:
    def __init__(self, nums) -> None:
        self.nums = nums
        self.tree = [0 for _ in range(4*len(nums))]

    def build(self, node, start, end):
        if start==end:
            self.tree[node] = {self.nums[start] : 1}
            return self.tree[node]
        
        mid = (start+end)//2
        left = self.build(2*node, start, mid)
        right = self.build(2*node+1, mid+1, end)

        self.tree[node] = {}
        for d in (left, right):
            for k, v in d.items():
                self.tree[node][k] = self.tree[node].get(k, 0) + v
        return self.tree[node]
    
    def rangeQuery(self, leftQuery, rightQuery, leftRange, rightRange, node, val):

        if leftRange>=leftQuery and rightRange<=rightQuery:
            if self.tree[node].get(val):
                return self.tree[node][val]
            return 0
        
        if leftRange>rightQuery or rightRange<leftQuery:
            return 0
        
        mid = (leftRange + rightRange)//2
        leftSum = self.rangeQuery(leftQuery, rightQuery, leftRange, mid, 2*node, val)
        rightSum = self.rangeQuery(leftQuery, rightQuery, mid+1, rightRange, 2*node+1, val)

        return leftSum+rightSum



    def __repr__(self) -> str:
        return str(self.__dict__)
    
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.segTree = SegmentTree(arr)
        self.segTree.build(1, 0, len(arr)-1)

    def query(self, left: int, right: int, value: int) -> int:
        return self.segTree.rangeQuery(left, right, 0, len(self.arr)-1,1,value)
    
    def __repr__(self) -> str:
        return str(self.__dict__)

obj = RangeFreqQuery([1,2,3,5,3,6,5,3,1])
param_1 = obj.query(0,8,5)
print(param_1)


'''
Problem : https://leetcode.com/problems/range-frequency-queries/
Approach :
1.The SegmentTree class represents the segment tree data structure. It has an array tree to store the frequency dictionaries at each node and a list nums to store the input array.
2.The build method is used to construct the segment tree. It takes the current node, start index, and end index as parameters. It recursively builds the segment tree by dividing the range in half until the start and end indices are equal.
3.At each node, the frequency dictionary for that range is constructed by merging the dictionaries of its left and right child nodes. The merged dictionary is stored in self.tree[node]. The merging process iterates over the dictionaries left and right, and for each key-value pair, it updates the frequency dictionary of the current node.
4.The rangeQuery method is used to perform a range query on the segment tree. It takes the query range (leftQuery and rightQuery), the current range represented by the node (leftRange and rightRange), the current node, and the value to query as parameters.
5.If the current range is completely within the query range, it checks if the frequency dictionary of the current node contains the given value. If it does, it returns the frequency value; otherwise, it returns 0.
6.If the current range is completely outside the query range, it returns 0.
7.If the current range partially overlaps with the query range, it recursively calls the rangeQuery method on its left and right child nodes and sums up the results.
8.The RangeFreqQuery class encapsulates the segment tree and provides a query method to perform range frequency queries. It initializes the segment tree in its constructor by calling the build method of the SegmentTree class.
9.The query method takes the left and right indices of the query range and the value to query. It calls the rangeQuery method of the segment tree with the appropriate parameters and returns the result.
'''
