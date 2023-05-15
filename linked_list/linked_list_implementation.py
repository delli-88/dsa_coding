class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return str(self.__dict__)

class LinkedList:
    def __init__(self):
        self.lenght = 0
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        return str(self.__dict__)

    def prepend(self,val):
        new_node = Node(val)
        if self.head==None:
            self.head = new_node
            self.tail = self.head    
        else:
            new_node.next = self.head
            self.head = new_node
        self.lenght+=1

    def append(self,val):
        new_node = Node(val)
        if self.head==None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght+=1

    def insert(self,pos,val):
        if pos>self.lenght or pos<0:
            print("Not Possible")
        else:
            if pos==0:
                self.prepend(val)
            elif pos==self.lenght:
                self.append(val)
            else:
                new_node = Node(val)
                curr = self.head
                for _ in range(pos-1):
                    curr = curr.next
                new_node.next = curr.next
                curr.next = new_node
                self.lenght+=1

    def delete_first(self):
        if self.head==None:
            print("Not possible")
        elif self.head==self.tail:
            self.head = self.head.next
            self.tail = self.tail.next
            self.lenght-=1
        else:
            self.head = self.head.next
            self.lenght-=1

    def delete_last(self):
        if self.head==None:
            print("Not possible")
        elif self.head==self.tail:
            self.head = self.head.next
            self.tail = self.tail.next
            self.lenght-=1
        else:
            curr = self.head
            for _ in range(self.lenght-2):
                curr = curr.next
            curr.next = None
            self.tail = curr
            self.lenght-=1
    def delete_by_pos(self,index):
        if index<0 or index>=self.lenght:
            print("Not Posible")
        elif index==0:
            self.delete_first()
        elif index==self.lenght-1:
            self.delete_last()
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
            self.lenght-=1

    def delete_by_val(self,val):
        if self.head==None:
            print("Not Possible")
        elif self.head==self.tail:
            if self.head.data==val:
                self.head = None
                self.tail = self.head
                self.lenght-=1
            else:
                print("Value Not Found")
        else:
            if self.head.data==val:
                self.head = self.head.next
                self.lenght-=1
            else:
                prev = self.head
                curr = self.head.next
                while curr!=None:
                    if curr.data==val:
                        prev.next = curr.next
                        if prev.next==None:
                            self.tail = prev
                        self.lenght-=1
                        break
                    curr = curr.next
                    prev = prev.next
                else:
                    print("Value Not Found")



    def print_linked_list(self):
        if self.lenght>0:
            temp = self.head
            while temp.next!=None:
                print(f"{temp.data} ->",end=" ")
                temp = temp.next
            print(f"{temp.data}")
        else:
            print("No Nodes")
            

myLL = LinkedList()
# myLL.prepend(2)
# myLL.prepend(4)
# myLL.prepend(3)
myLL.append(5)
myLL.append(6)
myLL.append(7)
myLL.append(8)
myLL.append(9)
# myLL.insert(0,1)
# myLL.insert(7,8)
# myLL.insert(2,9)
# myLL.delete_first()
# myLL.delete_last()
# myLL.delete_by_pos(1)
# myLL.delete_by_val(8)
# print(myLL)
myLL.print_linked_list()
