from typing import List

class SegmentTreeNode:
    def __init__(self, start: int, end: int, x_cords: List[int]) -> None:
        self.start = start
        self.end = end
        self.total = 0
        self.count = 0
        self.left = None
        self.right = None
        self.x_cords = x_cords

    def update(self, i: int, j: int, val: int) -> int:
        if i >= j:
            return 0
        if self.start == i and self.end == j:
            self.count += val
        else:
            mid = (self.start + self.end) // 2
            if j <= mid:
                if self.left is None:
                    self.left = SegmentTreeNode(self.start, mid, self.x_cords)
                self.left.update(i, j, val)
            elif i >= mid:
                if self.right is None:
                    self.right = SegmentTreeNode(mid, self.end, self.x_cords)
                self.right.update(i, j, val)
            else:
                if self.left is None:
                    self.left = SegmentTreeNode(self.start, mid, self.x_cords)
                self.left.update(i, mid, val)
                if self.right is None:
                    self.right = SegmentTreeNode(mid, self.end, self.x_cords)
                self.right.update(mid, j, val)
        if self.count > 0:
            self.total = self.x_cords[self.end] - self.x_cords[self.start]
        else:
            self.total = (self.left.total if self.left else 0) + (self.right.total if self.right else 0)
        return self.total
    
    def __repr__(self) -> str:
        return str(self.__dict__)

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:

        events = []
        
        x_cords = set()
        for x1, y1, x2, y2 in rectangles:
            if x1 < x2 and y1 < y2:
                events.append((y1, 1, x1, x2))
                events.append((y2, -1, x1, x2))
                x_cords.add(x1)
                x_cords.add(x2)
        events.sort()
        if not events:
            return 0
        x_cords = sorted(x_cords)
        x_indices= {x_cords[i]: i for i in range(len(x_cords))}
        active = SegmentTreeNode(0, len(x_cords) - 1, x_cords)
        area = 0
        cum_x_sum = 0
        curr_y = events[0][0]

        for y, type, x1, x2 in events:
            area += cum_x_sum * (y - curr_y)
            cum_x_sum = active.update(x_indices[x1], x_indices[x2], type)
            curr_y = y

        return area % (10 ** 9 + 7)
    
    def __repr__(self) -> str:
        return str(self.__dict__)



print(Solution().rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))


'''
Problem : https://leetcode.com/problems/rectangle-area-ii/
Approach : 
1.Create the SegmentTreeNode class:
    a.The SegmentTreeNode class represents a node in the segment tree.
    b.Each node contains the start and end indices representing the x-coordinate range it covers, the total width covered by active rectangles within that range, the count of active rectangles, and references to the left and right child nodes.
    c.The class also stores the list of x-coordinates.
2.Implement the update method in the SegmentTreeNode class:
    a.The update method updates the segment tree based on the given range (i to j) with a specified value (val).
    b.If the range is invalid (i.e., i >= j), it returns 0.
    c.If the node's range matches the given range exactly, it updates the count of active rectangles (self.count) by adding the given value.
    d.If the node's range does not match the given range exactly, it recursively calls update on the appropriate child nodes based on the split point (mid).
    e.After updating the count, the total attribute is updated to reflect the total width covered by active rectangles within the node's range.
3.Implement the rectangleArea method in the Solution class:

    a.The rectangleArea method takes a list of rectangles as input and calculates the total area covered by those rectangles.
    b.It creates a list of events, where each event contains the y-coordinate, type (1 for opening, -1 for closing), and the x-coordinates of the corresponding rectangle.
    c.The events are sorted in ascending order based on the y-coordinate.
    d.If the events list is empty, it means there are no rectangles, so the method returns 0.
    e.The x-coordinates are sorted and assigned indices for efficient access.
    f.The method initializes an instance of SegmentTreeNode (active) to represent the entire x-coordinate range.
    g.It iterates through the events in sorted order and calculates the area incrementally.
        i.For each event, it adds the product of cum_x_sum (cumulative sum of x-differences) and the difference between the current y-coordinate and the previous y-coordinate to the area.
        ii.It updates cum_x_sum by calling the update method on the active segment tree node, passing the x-indices of the corresponding x-coordinates and the type of the event (1 for opening, -1 for closing).
        iii.Finally, it updates curr_y to the current y-coordinate.
    h.The method returns the calculated area modulo (10 ** 9 + 7).
'''