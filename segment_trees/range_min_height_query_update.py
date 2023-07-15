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
        self.tree[node] =  min(left,right) 

        return self.tree[node]
    
    def minQuery(self, leftQuery, rightQuery, leftRange, rightRange, node):

        if leftRange>=leftQuery and rightRange<=rightQuery:
            return self.tree[node]
        
        if leftRange>rightQuery or rightRange<leftQuery:
            return float("inf")
        
        mid = (leftRange + rightRange)//2
        leftMin = self.minQuery(leftQuery, rightQuery, leftRange, mid, 2*node)
        rightMin = self.minQuery(leftQuery, rightQuery, mid+1, rightRange, 2*node+1)

        return min(leftMin,rightMin)
    
    def update(self, ind, val, leftRange, rightRange, node):
        if leftRange==ind and rightRange==ind:
            self.tree[node] = val
            return self.tree[node]
        
        if leftRange>ind or rightRange<ind:
            return self.tree[node]
        
        mid = (leftRange+rightRange)//2

        left_min = self.update(ind, val, leftRange, mid, 2*node)

        right_min  = self.update(ind, val, mid+1, rightRange, 2*node+1)
        
        self.tree[node] = min(left_min, right_min)

        return self.tree[node]


    def __repr__(self) -> str:
        return str(self.__dict__)

def lilliput(n: int, height: List[int] , q: int, queries: list) -> List[int]:
    segTreeObj = SegmentTree(height)
    segTreeObj.build(1, 0, n-1)

    sol = []
    for i in range(q):
        if queries[i][0]=="q":
            sol.append(segTreeObj.minQuery(queries[i][1],queries[i][2],0,n-1,1))
        else:
            segTreeObj.update(queries[i][1],queries[i][2],0,n-1,1)
    return sol

print(lilliput(5,[2,3,5,1,9],4,[["q",0,2],["u",1,0],["q",1,4],["q",3,3]]))


'''
1.Create a SegmentTree class that represents the segment tree data structure.
2.Initialize the SegmentTree class with the input list nums. This will create an empty tree with the appropriate size to store the minimum values.
3.Implement the build method in the SegmentTree class to build the segment tree recursively. Starting from the root node (index 1), divide the range into two halves and recursively build the left and right subtrees.
4.In the minQuery method, recursively traverse the segment tree to find the minimum value in the specified range [leftQuery, rightQuery]. Compare the range of each node with the query range and recursively traverse to the left or right subtree depending on the conditions.
5.In the update method, recursively update the value of the segment tree for the specified index ind with the new value val. Traverse the tree recursively and update the nodes in the path to the specified index.
6.Implement the lilliput function to solve the Lilliput problem. Initialize a SegmentTree object with the height list. Build the segment tree using the build method.
7.Iterate through the queries list. If the query is of type "q", call the minQuery method to find the minimum height in the specified range and append it to the result list sol. If the query is of type "u", call the update method to update the height at the specified index.
8.Return the result list sol.
'''