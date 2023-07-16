
from typing import List

class SegTreeNode:
    def __init__(self, xarr, st, ed):
        self.xCoords = xarr
        self.start = st
        self.end = ed
        self.left = None
        self.right = None
        self.isleave = False
        self.count = 0
        self.total = 0
    
    def __repr__(self) -> str:
        return str(self.__dict__)

def getMid(i, j):
    return i + (j - i) // 2

def buildTree(xCoords, i, j):
    if i >= j:
        return None
    cur = SegTreeNode(xCoords, i, j)
    if j - i == 1:
        cur.isleave = True
    else:
        cur.left = buildTree(xCoords, i, getMid(i, j))
        cur.right = buildTree(xCoords, getMid(i, j), j)
    return cur

def update(root, startIdx, endIdx, countUpdate):
    if root.end <= startIdx or root.start >= endIdx:
        return
    if root.isleave:
        root.count += countUpdate
        root.total = root.count > 0 and root.xCoords[root.end] - root.xCoords[root.start] or 0
    else:
        update(root.left, startIdx, endIdx, countUpdate)
        update(root.right, startIdx, endIdx, countUpdate)
        root.total = root.left.total + root.right.total
    return

def query(root, i, j):
    if i < root.start or j > root.end:
        return 0
    if i <= root.end and j >= root.start:
        return root.total
    else:
        return query(root.left, i, j) + query(root.right, i, j)

def rectangleArea(rectangles):
    OPEN = 1
    CLOSE = -1
    events = [[rec[1], OPEN, rec[0], rec[2]] for rec in rectangles] + [[rec[3], CLOSE, rec[0], rec[2]] for rec in rectangles]
    Xvals = set()
    for rec in rectangles:
        Xvals.add(rec[0])
        Xvals.add(rec[2])
    
    events.sort(key=lambda x: x[0])
    
    X = sorted(list(Xvals))
    Xi = {xval: i for i, xval in enumerate(X)}
    
    root = buildTree(X, 0, len(X))
    ans = 0
    cur_x_sum = 0
    cur_y = events[0][0]
    
    for event in events:
        y, typ, x1, x2 = event
        ans += cur_x_sum * (y - cur_y)
        update(root, Xi[x1], Xi[x2], typ)
        cur_x_sum = query(root, root.start, root.end)
        cur_y = y
    
    ans %= (pow(10,9) + 7)
    return int(ans)

print(rectangleArea(rectangles=[[0,0,2,2],[1,0,2,3],[1,0,3,1]]))

'''
Problem : https://leetcode.com/problems/rectangle-area-ii/
Approach :
'''



'''
# TLE
from typing import List
class SegmentTree:
    def __init__(self, nums, x_max, y_max) -> None:
        self.nums = nums
        self.tree = [[0 for _ in range(4*x_max)] for _ in range(y_max)]

    
    def update(self, ind, y,val, leftRange, rightRange, node):
        if leftRange==ind and rightRange==ind:
            result = 0
            if self.tree[y][node]==0:
                self.tree[y][node] = 1
                result = 1

            return result
        
        mid = (leftRange+rightRange)//2
        if ind<=mid:
            result = self.update(ind, y,val, leftRange, mid, 2*node)
        else:
            result = self.update(ind, y,val, mid+1, rightRange, 2*node+1)
        
        self.tree[y][node]+=result

        return result


    def __repr__(self) -> str:
        return str(self.__dict__)
    
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        (x_max, y_max) = self.findXYmax(rectangles)

        seg_tree = SegmentTree(rectangles, x_max, y_max)

        for i in range(len(rectangles)):
            bot_x, bot_y, top_x, top_y = rectangles[i]

            for y in range(bot_y, top_y):
                for x in range(bot_x, top_x):
                    seg_tree.update(x,y,1,0, x_max-1, 1)

        area = 0
        for i in range(len(seg_tree.tree)):
            area+= seg_tree.tree[i][1]

        return area
    
    def findXYmax(self, matrix):
        xMax = 0
        yMax = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j%2==0:
                    xMax = max(xMax, matrix[i][j])
                else:
                    yMax = max(yMax, matrix[i][j])
        
        return (xMax, yMax)


    
print(Solution().rectangleArea(rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]))
'''
