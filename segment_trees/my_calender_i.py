
class Node:
    def __init__(self, low, high) -> None:
        self.low = low
        self.high = high
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self.__dict__)

class MyCalendar:

    def __init__(self):
        self.my_seg_tree = None
        self.available = False

    def book(self, start: int, end: int) -> bool:
        if self.my_seg_tree==None:
            self.my_seg_tree = Node(start, end)
            return True
        
        self.update(self.my_seg_tree, start, end)
        isAvailable = self.available
        self.available = False

        return isAvailable  
        
    def update(self,root,start, end):

        if root==None:
            self.available = True
            return Node(start, end)
        
        if end<=root.low:
            root.left = self.update(root.left, start, end)
        
        elif start>=root.high:
            root.right = self.update(root.right, start, end)
        
        return root

    def __repr__(self) -> str:
        return str(self.__dict__)



obj = MyCalendar()
param_1 = obj.book(10,20)
param_2 = obj.book(15,20)
param_3 = obj.book(20,30)
param_4 = obj.book(1,7)


print(param_1)
print(obj.my_seg_tree)

